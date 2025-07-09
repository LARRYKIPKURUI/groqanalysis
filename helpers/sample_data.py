sample_user_details = {
    "user_id": 101,
    "name": "Jane Mwende",
    "email": "jane.mwende@retailforce.ke",
    "role": "Field Representative",
    "department": "Nairobi Region",
    "is_active": True
}

sample_workflow_data = {
    "success": True,
    "data": {
        "user_id": 101,
        "itenary_id": 1001,
        "category_id": 5,
        "flow_status": {
            "total_steps": 4,
            "completed_steps": 3,
            "pending_steps": 1,
            "error_steps": 0,
            "completion_percentage": 75,
            "is_complete": False,
            "has_errors": False,
            "latest_activity": "2025-07-08 15:00"
        },
        "flow_data": {
            "stock_check": {
                "step_name": "Stock Check",
                "status": "completed",
                "count": 12,
                "last_updated": "2025-07-08 13:00",
                "data": ["SKU001", "SKU002", "SKU003"]
            },
            "photo_upload": {
                "step_name": "Photo Upload",
                "status": "completed",
                "count": 3,
                "last_updated": "2025-07-08 13:10",
                "data": ["front_display.jpg", "shelf.jpg", "checkout.jpg"]
            },
            "survey_entry": {
                "step_name": "Survey Entry",
                "status": "pending",
                "count": 0,
                "last_updated": "N/A",
                "data": []
            },
            "store_exit": {
                "step_name": "Store Exit",
                "status": "completed",
                "count": 1,
                "last_updated": "2025-07-08 13:45",
                "data": ["Exit confirmed"]
            }
        },
        "tracking_metadata": {
            "date_range": {
                "from": "2025-07-08",
                "to": "2025-07-08"
            },
            "location": "Nairobi Westgate",
            "device_used": "Samsung Galaxy A32"
        }
    }
}
