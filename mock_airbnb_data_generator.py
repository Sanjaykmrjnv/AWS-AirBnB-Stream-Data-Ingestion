import json
import boto3
import random
import uuid
from datetime import datetime, timedelta

sqs_client = boto3.client('sqs')
QUEUE_URL = ''

def generator_Airbnb_booking():
    location = random.choice(["New York, USA", "Paris, France", "Tokyo, Japan", "London, UK", "Sydney, Australia", "New Delhi, India", "Noida, India"])
    
    start_date = datetime.now() - timedelta(days=random.randint(1, 365))
    end_date = start_date + timedelta(days=random.randint(1, 30))

    return{
        "bookingId": str(uuid.uuid4()),
        "userId": random.randint(1,99),
        "propertyId": random.randint(100,999),
        "location": location,
        "startDate": start_date.strftime('%Y-%m-%d'),
        "endDate": end_date.strftime('%Y-%m-%d'),
        "price": round(random.uniform(10.0,1000.0),2)
    }

def lambda_handler(event,context):
    i = 0
    while(i<5):
        airbnb_booking_data = generator_Airbnb_booking
        print(airbnb_booking_data)
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(airbnb_booking_data)
        )
        i += 1

    return {
        'statusCode': 200,
        'body': json.dumps('Booking data published to SQS!')
    }