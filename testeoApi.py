#PASO 1. IMPORTAR EL MODELO
import google.generativeai as genai

#PASO 2. CONFIGURAR LA API
genai.configure(api_key="")

#PASO 3. CREAR EL MODELO
modelo=genai.GenerativeModel("gemini-2.0-flash-lite")

#PASO 4. VERIFICAR EL MODELO
pregunta=input("Ingrese su pregunta: ")
respuesta=modelo.generate_content(pregunta)
print(respuesta)
