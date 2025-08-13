from fastapi import FastAPI, HTTPException, Depends
from database import initialize_database, initialize_conn_and_cursor, DB_NAME
from models import AddAddress, UpdateAddress, GetCoordinates
import math

app = FastAPI(title="Address Book API")

# Initialize Database
initialize_database()

# ================
# API ENDPOINTS ||
# ================


@app.get("/health")
def health_check():
    return {"status": "healthy"}

# ==========================
# Add address to database ||
# ==========================
@app.post("/address")
def add_address(address: AddAddress):
    try:
        conn, cursor = initialize_conn_and_cursor(DB_NAME)
    
        cursor.execute("""
                    INSERT INTO address(address, label, longitude, latitude)
                    VALUES(?, ?, ?, ?)
                    """, (address.address, 
                            address.label, 
                            address.longitude, 
                            address.latitude))
        conn.commit()
        new_address = address.address
        label = address.label
        conn.close()
        
        return {"message": "Address succesfully created", "address": new_address, "label": label }
    except Exception as e:
        return f"Error: {e}"

# =============================
# Update address on database ||
# =============================

@app.put("/address/{address_id}")
def update_address(address_id: int, update_address: UpdateAddress):
    try:
        conn, cursor = initialize_conn_and_cursor(DB_NAME)
    
        cursor.execute("SELECT * FROM address WHERE address_id = ?", (address_id,))
        existing_address = cursor.fetchone()
        
        if not existing_address:
            conn.close()
            raise HTTPException(status_code=404, detail="Address not found on database")
        
        updated_values = {
            "label": update_address.label if update_address.label is not None else existing_address[1],
            "address": update_address.address if update_address.address is not None else existing_address[2],
            "latitude": update_address.latitude if update_address.latitude is not None else existing_address[3],
            "longitude": update_address.longitude if update_address.longitude is not None else existing_address[4],
        }
        
        cursor.execute("""
                        UPDATE address 
                        SET label = ?, address = ?, latitude = ?, longitude = ?
                        WHERE address_id = ?
                    """, (updated_values["label"], 
                            updated_values["address"], 
                            updated_values["latitude"], 
                            updated_values["longitude"], 
                            address_id))
        
        updated_address = updated_values["address"]
        
        conn.commit()
        conn.close()
        
        return {"message": f"Address: {updated_address}, successfully updated"}
    
    except Exception as e:
        return f"Error: {e}"


# ====================================================
# User retrieving data using longitude and latitude ||
# ====================================================

# formula to calculate nearby distance given the user's, latitude, longitude and addresses' latitude and longitude 
def haversine(user_latitude, user_longitude, latitude, longitude):
    R = 6371  # Earth radius in km

    # Convert degrees to radians
    user_latitude, user_longitude, latitude, longitude = map(math.radians, [user_latitude, user_longitude, latitude, longitude])

    # Differences
    dlat = latitude - user_latitude
    dlon = longitude - user_longitude

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(user_latitude) * math.cos(latitude) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

# function to create a Pydantic model from query params
def get_coordinates(latitude: float, longitude: float, radius: int) -> GetCoordinates:
    return GetCoordinates(latitude=latitude, longitude=longitude, radius=radius)

@app.get("/address/nearby_address")
def get_address(coordinates: GetCoordinates = Depends(get_coordinates)):
    try:
        conn, cursor = initialize_conn_and_cursor(DB_NAME)
    
        cursor.execute("SELECT address, label, latitude, longitude FROM address")
        rows = cursor.fetchall()
        
        conn.close()
        
        nearby_addresses = []
        
        for row in rows:
            address, label, latitude, longitude = row
            address_coordinates = haversine(coordinates.latitude, coordinates.longitude, latitude, longitude)
            
            if address_coordinates <= coordinates.radius:
                nearby_addresses.append({
                    "address": address,
                    "label": label,
                    "latitude": latitude,
                    "longitude": longitude
                })
        
        if not nearby_addresses:
            raise HTTPException(status_code=404, detail="No address found with your coordinates.")
    
        return {"message": f"Address/es found {nearby_addresses}"}
    except Exception as e:
        return f"Error: {e}"

# =============================
# Delete address on database ||
# =============================

@app.delete("/address/{address_id}")
def delete_address(address_id: int):
    try:
        conn, cursor = initialize_conn_and_cursor(DB_NAME)
    
        cursor.execute("DELETE FROM address WHERE address_id = ?", (address_id,))
        conn.commit()
        
        deleted_row = cursor.rowcount
        
        conn.close()
        
        if deleted_row == 0:
            raise HTTPException(status_code=404, detail="Address not found on database")
        
        return {"message": f"Address: {address_id} successfully deleted"}
    except Exception as e:
        return f"Error: {e}"