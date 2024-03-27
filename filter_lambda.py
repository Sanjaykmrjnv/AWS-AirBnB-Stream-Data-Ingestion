import json
import datetime

def calculate_duration(start_date, end_date):
    try:
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        duration = (end - start).days
        return duration
    except ValueError:
        print("Error parsing date format. Skipping message.")
        return None  # Or handle the error differently

def lambda_handler(event, context):
    print("Event", event)
    processed_messages = []
    
    # Iterate over the elements of the 'event' list
    for record in event:
        # Parse incoming message
        message = json.loads(record['body'])
        print("message",message)
        
        # Calculate booking duration
        start_date = message.get('startDate')
        end_date = message.get('endDate')
        
        if start_date is None or end_date is None:
            print("Missing start date or end date. Skipping message.")
            continue
        
        booking_duration = calculate_duration(start_date, end_date)
        
        if booking_duration is not None and booking_duration > 1:
            # Message passes the filter, add to processed messages
            processed_messages.append(message)
            print("Booking duration is more than 1 day. Proceeding with processing.")
            print("Processed Message",processed_messages)
        elif booking_duration is not None and booking_duration <= 1:
            # Message does not pass the filter, skip processing
            print("Booking duration is not more than 1 day. Skipping processing.")
        else:
            # Handle the case where duration calculation failed
            print("Booking duration could not be calculated. Skipping processing.")
    
    return {
        'statusCode': 200,
        'body': json.dumps(processed_messages)
    }
