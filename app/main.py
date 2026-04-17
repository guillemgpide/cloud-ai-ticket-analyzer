from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from model.classifier import analyze_ticket
import datetime

app = FastAPI(title="Cloud-AI Support Ticket Analyzer")

class Ticket(BaseModel):
    user_id: str
    message: str

# INTERFICIE USER
@app.get("/", response_class=HTMLResponse)
async def web_ui():
    html_content = """
        <!DOCTYPE html>
        <html lang="ca">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Analitzador de Tiquets IA</title>
            <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="bg-gray-50 h-screen flex items-center justify-center font-sans">
            
            <div class="bg-white p-8 rounded-2xl shadow-xl max-w-lg w-full border border-gray-100">
                <div class="flex items-center space-x-3 mb-6">
                    <div class="bg-blue-600 p-2 rounded-lg"><span class="text-xl">🤖</span></div>
                    <div>
                        <h1 class="text-2xl font-bold text-gray-800">IA Support Desk</h1>
                        <p class="text-sm text-gray-500">Classificació automàtica de tiquets</p>
                    </div>
                </div>
                
                <textarea id="ticketText" rows="4" 
                    class="w-full p-4 border border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent outline-none transition-all resize-none mb-4 shadow-sm" 
                    placeholder="Escriu el teu problema aquí. Ex: La factura és un desastre..."></textarea>
                
                <button id="btnAnalitzar" onclick="enviarTiquet()" 
                    class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-4 rounded-xl transition duration-200 shadow-md flex justify-center items-center">
                    <span>Analitzar Missatge</span>
                </button>

                <div id="resultat" class="mt-6 hidden opacity-0 transition-opacity duration-500">
                    <h3 class="font-semibold text-gray-700 border-b border-gray-100 pb-2 mb-4 text-sm uppercase tracking-wider">Resultat del Núvol</h3>
                    
                    <div class="grid grid-cols-2 gap-4">
                        <div class="bg-blue-50 p-4 rounded-xl border border-blue-100 text-center">
                            <span class="block text-xs text-blue-500 uppercase font-bold mb-1">Categoria</span>
                            <span id="resCategoria" class="text-lg font-semibold text-blue-800"></span>
                        </div>
                        <div class="bg-purple-50 p-4 rounded-xl border border-purple-100 text-center">
                            <span class="block text-xs text-purple-500 uppercase font-bold mb-1">Sentiment</span>
                            <span id="resSentiment" class="text-lg font-semibold text-purple-800"></span>
                        </div>
                    </div>
                    
                    <button onclick="nouTiquet()" 
                        class="mt-6 w-full bg-gray-100 hover:bg-gray-200 text-gray-700 font-semibold py-2 px-4 rounded-xl transition duration-200 border border-gray-300 flex justify-center items-center space-x-2">
                        <span>📝 Escriure un nou tiquet</span>
                    </button>
                </div>
            </div>

            <script>
                async function enviarTiquet() {
                    const text = document.getElementById('ticketText').value;
                    if (!text) return;
                    
                    const boto = document.getElementById('btnAnalitzar');
                    // Desactivem el botó i mostrem spinner
                    boto.disabled = true;
                    boto.classList.add('opacity-75', 'cursor-not-allowed');
                    boto.innerHTML = `<svg class="animate-spin h-5 w-5 mr-3 text-white" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> Processant...`;
                    
                    const response = await fetch('/analyze', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ user_id: 'web_user', message: text })
                    });
                    
                    const data = await response.json();
                    
                    document.getElementById('resCategoria').innerText = data.ai_analysis.category;
                    const sentiment = data.ai_analysis.sentiment;
                    let emoji = sentiment === 'Positive' ? '😊 ' : (sentiment === 'Negative' ? '😡 ' : '😐 ');
                    document.getElementById('resSentiment').innerText = emoji + sentiment;
                    
                    const divResultat = document.getElementById('resultat');
                    divResultat.classList.remove('hidden');
                    setTimeout(() => divResultat.classList.remove('opacity-0'), 50);
                    
                    // Restaurem el botó principal
                    boto.innerHTML = "<span>Analitzar Missatge</span>";
                    boto.disabled = false;
                    boto.classList.remove('opacity-75', 'cursor-not-allowed');
                }

                // NOVA FUNCIÓ: Neteja la UI sense recarregar la pàgina
                function nouTiquet() {
                    // 1. Buidem la caixa de text
                    document.getElementById('ticketText').value = '';
                    
                    // 2. Amaguem la caixa de resultats suaument
                    const divResultat = document.getElementById('resultat');
                    divResultat.classList.add('opacity-0');
                    
                    // Esperem mig segon a que acabi l'animació de desaparèixer abans d'ocultar l'element
                    setTimeout(() => {
                        divResultat.classList.add('hidden');
                    }, 500);
                }
            </script>
        </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)

# REP DADES
@app.post("/analyze")
async def process_ticket(ticket: Ticket):
    analysis = analyze_ticket(ticket.message)
    result = {
        "user_id": ticket.user_id,
        "original_message": ticket.message,
        "ai_analysis": analysis,
        "timestamp": datetime.datetime.now().isoformat(),
        "status": "stored_in_cloud"
    }
    return result