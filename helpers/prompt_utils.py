def create_prompt_from_workflow_data(workflow_data, user_details=None):
    try:
        if not workflow_data.get("success"):
            return "No workflow data available for analysis."

        data = workflow_data.get("data", {})
        user_id = data.get("user_id")
        itenary_id = data.get("itenary_id")
        category_id = data.get("category_id")

        user_name = user_details.get("name", f"User {user_id}")
        user_role = user_details.get("role", "Field Representative")
        user_email = user_details.get("email", "")
        user_department = user_details.get("department", "")

        flow_status = data.get("flow_status", {})
        flow_data = data.get("flow_data", {})

        prompt = f"""
RETAIL FIELD PERFORMANCE DATA ANALYSIS

FIELD REPRESENTATIVE DETAILS:
User ID: {user_id}
Name: {user_name}
Role: {user_role}
Email: {user_email}
Department: {user_department}

WORKFLOW OVERVIEW:
Itinerary ID: {itenary_id}
Category ID: {category_id}

WORKFLOW COMPLETION STATUS:
- Total Steps: {flow_status.get('total_steps', 0)}
- Completed Steps: {flow_status.get('completed_steps', 0)}
- Pending Steps: {flow_status.get('pending_steps', 0)}
- Error Steps: {flow_status.get('error_steps', 0)}
- Completion Percentage: {flow_status.get('completion_percentage', 0)}%
- Latest Activity: {flow_status.get('latest_activity', 'N/A')}

DETAILED WORKFLOW DATA:
"""

        for step_key, step_data in flow_data.items():
            step_name = step_data.get('step_name', step_key)
            prompt += f"""
{step_name.upper()}:
- Status: {step_data.get('status')}
- Data Count: {step_data.get('count')}
- Last Updated: {step_data.get('last_updated')}
"""

            if step_data.get('data'):
                prompt += f"- Sample Data: {step_data['data'][:3]}\n"

            if step_data.get('error'):
                prompt += f"- Error: {step_data['error']}\n"

        metadata = data.get("tracking_metadata", {})
        prompt += f"""
TRACKING METADATA:
- Date Range: {metadata.get('date_range')}
- Location: {metadata.get('location')}
- Device Used: {metadata.get('device_used')}

ANALYSIS INSTRUCTIONS FOR AI:
Please analyze this data for {user_name} ({user_role}) and provide personalized, actionable insights.
NEVER refer to them as "User {user_id}". Always use "{user_name}".
"""

        return prompt

    except Exception as e:
        return f"Prompt error: {str(e)}"
