# 🚀 Desafio Final: Executando Tarefas Automatizadas com AWS Lambda e Amazon S3 ☁️

## 📘 Descrição do Projeto

Este projeto foi desenvolvido como parte do desafio **“Executando Tarefas Automatizadas com Lambda Function e S3”** do **BootCamp Santander Code Girls 2025 | DIO**.

O objetivo foi aplicar, na prática, os conceitos de **CloudFormation, S3 Object Lambda** e **funções Lambda** para automatizar tarefas dentro do ambiente AWS.  
Durante o processo, explorei a criação de buckets, funções Lambda, Access Points e a implementação de templates via **CloudFormation**, consolidando meus conhecimentos sobre automação na nuvem.

---

## 🎯 Objetivos de Aprendizagem

Ao finalizar este laboratório, foi possível:

- Criar e configurar **Buckets S3** e **Access Points**;
- Implementar **Lambda Functions** para processar objetos automaticamente;
- Utilizar **CloudFormation Templates** para automatizar a criação dos recursos;
- Documentar o processo técnico de forma clara e estruturada;
- Utilizar o **GitHub** como ferramenta de compartilhamento de documentação técnica.

---

## 🧩 Arquitetura do Projeto

A estrutura criada é composta pelos seguintes componentes:

- **Amazon S3 Bucket** → Armazena os objetos que serão processados.  
- **Supporting Access Point (AP)** → Fornece o acesso padrão ao bucket.  
- **Object Lambda Access Point (OLAP)** → Permite que o Lambda modifique dados do S3 em tempo real.  
- **AWS Lambda Function** → Executa o processamento automático de objetos.  
- **AWS CloudFormation Stack** → Automatiza a criação de toda a infraestrutura.

---

## ⚙️ Passo a Passo — Implementação via Console AWS

### 🪣 1. Criar Bucket S3
1. Acesse o console da AWS → **Amazon S3** → **Criar bucket**.  
2. Nomeie o bucket (ex: `meu-bucket-lambda`).  
3. Selecione a região desejada e clique em **Criar bucket**.  

📌 *Esse bucket armazenará os arquivos que serão processados pela Lambda.*

---

### 🧠 2. Criar Função Lambda
1. Acesse o console → **Lambda** → **Criar função**.  
2. Escolha **Autor a partir do zero**.  
3. Nome: `lambda-olap-jullia`  
4. Runtime: **Python 3.11**  
5. Permissões: **Criar nova role com permissões básicas do Lambda**.  
6. Clique em **Criar função**.

Após criada:
- Vá até **Código-fonte** → cole o código do seu script (exemplo abaixo).
- Clique em **Implantar**.

```python
import boto3

def lambda_handler(event, context):
    print("Evento recebido:", event)
    return {"statusCode": 200, "body": "Processamento concluído com sucesso!"}
```
---
### 🔗 3. Criar Access Points

1. No console S3, abra o menu lateral e clique em Access Points.
2. Crie um **Access Point de suporte**:
  - Nome: supporting-ap-jullia
  - Bucket: meu-bucket-lambda
  - Permita acesso à função Lambda.
3. Depois, crie um **Object Lambda Access Point**:
  - Nome: objectlambda-jullia
  - Baseado no access point anterior.
  - Associe a função Lambda criada.
---

### ☁️ 4. Criar Stack no CloudFormation

1. Vá até o console → **CloudFormation** → Criar stack → *Com novos recursos (padrão)*.
2. Faça upload do template (`s3-lambda-template.yaml`).
3. Configure os parâmetros:

| Parâmetro |	**Valor**	| **Exemplo** |
| ------------ | ----------- | ------------ |
| **S3BucketName** |	Nome do bucket S3 |	`meu-bucket-lambda` |
| **SupportingAccessPointName** |	Nome do Access Point de suporte |	`supporting-ap-jullia` |
| **ObjectLambdaAccessPointName** |	Nome do Access Point Lambda	| `objectlambda-jullia` |

4. Clique em Próximo → Criar stack.
5. Aguarde até o status ser **CREATE_COMPLETE** ou no meu caso **ROLLBACK_COMPLETE**.

---
### 🧪 5. Testar a Função Lambda

1. Vá até o console Lambda → selecione a função → **Testar**.
2. Crie um evento de teste:
   ```json
   {
    "Records": [
    {
      "s3": {
        "bucket": {"name": "meu-bucket-lambda"},
        "object": {"key": "arquivo-teste.txt"}
      }
    }
    ]
    }
   ```
3. Clique em **Executar Teste**.
4. Verifique os logs no **CloudWatch** -> deve aparecer a mensagem de sucesso.

---

### 🧠 Insights e Aprendizados

Durante a prática, compreendi na prática como:
  - Automatizar tarefas na AWS utilizando CloudFormation;
  - Usar o conceito de Object Lambda, permitindo personalização de objetos S3 em tempo real;
  - Integrar S3 e Lambda de forma segura e eficiente;
  - Aplicar boas práticas de documentação técnica no GitHub.

---

### 🧰 Tecnologias Utilizadas

- AWS S3
- AWS Lambda
- AWS CloudFormation
- AWS IAM
- Python 3.9
- GitHub

---

### 💬 Conclusão

Este desafio foi uma excelente oportunidade de colocar em prática a automação de recursos AWS, aplicando Lambda Functions e CloudFormation de forma integrada.
A experiência me ajudou a consolidar o entendimento sobre infraestrutura como código e automação de processos na nuvem.

---

### 📎 Links Úteis

- Documentação AWS S3 Object Lambda: (https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/olap-using-cfn-template.html)
- Documentação AWS Lambda: (https://docs.aws.amazon.com/lambda/)
- AWS CloudFormation Guide: (https://docs.aws.amazon.com/cloudformation/)
- GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)
- DIO Bootcamp Santander Code Girls 2025: (https://web.dio.me/track/6cd0de9d-d33d-4a18-9557-aa17a0ee6fcc)
  

---

## 💬 Autor
**Jullia Karolina de Paula**
- 💻Estudante de Análise e Desenvolvimento de Sistemas 
- 📍Brasil
- 🔗Linkedin:(https://www.linkedin.com/in/jullia-karolina-de-paula-89a93a283/)
- 📧Email: julliakarolinadev@gmail.com | julliakarolinadepauladev@gmail.com
- Bootcamp Santander Code Girls 2025 - AWS - Desafio Final: *Executando Tarefas Automatizadas com Lambda Function e S3* 

--- 

### 🌟 “A nuvem não é o limite, é o começo.” ☁️💻

---


