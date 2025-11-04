# Paso 1. Importar librerías necesarias
import google.generativeai as genai
from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler

# Paso 2. Configurar el modelo Gemini
genai.configure(api_key="")
modelo = genai.GenerativeModel("gemini-2.5-flash-lite-preview-09-2025")

# Paso 3. Configurar el token del bot
tokenTelegram = ""


#Cargar el conocimiento
def cargarConocimiento(archivo):
    conocimiento={}
    with open(archivo,"r",encoding="utf-8") as archivoC:
        for linea in archivoC:
            if ":" in linea:
                pregunta, respuesta=linea.strip().split(":",1)


#Cargar Archivo
with open("conocimiento.txt","r",encoding="utf-8") as file:
    conocimientoBase=file.read()


# Paso 4. Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy el asistente virtual de *Udabol*.\n\n💬 ¿Cuál es tu consulta?", parse_mode="Markdown")

#Comando /inicio

# Paso 5. Procesar los mensajes del usuario
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        mensajeUsuario = update.message.text
        print(f"[USUARIO]: {mensajeUsuario}")

        mensajeModelo=f"""Deberas usar el texto como conocimiento base para poder responder
        las preguntas del usuario, no deberas salirte del tema del conocimiento base, si obtienes 
        preguntas no relacionadas a la Universidad responder que eres el asistente academico de la universidad y que solo puedes ayudar 
        con temas respecto a la universidad, 
        Responde de forma clara y concisa lo mas coordial posible
        
        Conocimiento Base: {conocimientoBase}

        Pregunta del usuario: {mensajeUsuario}
        
        """

        # Mostrar acción "escribiendo..."
        await update.message.chat.send_action(action=ChatAction.TYPING)

        # Generar respuesta con Gemini
        respuesta = modelo.generate_content(mensajeModelo)

        await update.message.reply_text(respuesta.text)

       
    except Exception as e:
        print(f"[ERROR]: {e}")
        await update.message.reply_text(" Ocurrió un error al conectarse con el servidor.")

# Paso 6. Función principal para ejecutar el bot
def main():
    print("🤖 Bot iniciado correctamente...")
    print("👉 Enlace: https://t.me/programacionAvanzadaBot")

    app = ApplicationBuilder().token(tokenTelegram).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    # Ejecutar bot
    app.run_polling()

#Ejecutar
if __name__ == "__main__":
    main()
