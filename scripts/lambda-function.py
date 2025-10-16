import json
import boto3

def lambda_handler(event, context):
    print("Evento recebido:", json.dumps(event))
    
    # Exemplo de manipulação de objeto
    
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executada com sucesso!')
    }

