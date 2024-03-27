import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print("Event", event)
    
    # Extract the body of the first record in the event
    record_body = event[0]['body']
    
    # Write the record body to S3
    write_to_s3(record_body)
    
    return {
        'statusCode': 200,
        'body': json.dumps({"message": "Record written to S3"})
    }

def write_to_s3(data):
    bucket_name = 'airbnb-booking-records-sa'
    key = 'Filtered_Bookings.json'
    try:
        s3_client.put_object(
            Body=json.dumps(data),
            Bucket=bucket_name,
            Key=key
        )
        print("Record written to S3 as 'Filtered_Bookings.json'")
    except Exception as e:
        print(f"Error writing to S3: {e}")
