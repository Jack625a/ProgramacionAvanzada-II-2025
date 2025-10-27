#Api Telegram:  

#Paso 1. importar las librerias
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes,CommandHandler

#Paso 2. Configurar el modelo gemini
genai.configure(api_key="")
modelo=genai.GenerativeModel("gemini-2.5-flash-lite")

#Paso 3. Configurar el bot
tokenTelegram=''

#Paso 4. Configurar el comandos en telegram
async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola soy el asistente de Udabol. cual es tu consulta?...")

#Paso 5. Procesar los mensajes 
async def responder(update:Update, context:ContextTypes.DEFAULT_TYPE):
    try: 
        mensajeUsuario=update.message.text
        await update.message.chat.send_action("Escribiendo...")
        print(f"[USUARIO]: {mensajeUsuario}")
        respuesta=modelo.generate_content(mensajeUsuario)
        if respuesta and respuesta.text:
            texto=respuesta.text.strip()
        else: 
            texto="Error al procesar, vuelva a intentar..."
        await update.message.reply_text(texto)
    except Exception as e:
        print(f"[ERROR]: {e}")
        await update.message.reply_text("Ocurrio un error al conectarse con el servidor...")


#Paso 6. Crear la funcion principal
def main():
    app=ApplicationBuilder().token(tokenTelegram).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    #iniciar el bot
    print(f"Bot Inicado.... https://t.me/programacionAvanzadaBot")
    app.run_polling()

main()

