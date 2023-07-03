import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'messages.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages
                 (cmd TEXT, hostname TEXT, team TEXT, home TEXT, from_value TEXT)''')
    conn.commit()
    conn.close()

def insert_message(cmd, hostname, team, home, from_value):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)",
              (cmd, hostname, team, home, from_value))
    conn.commit()
    conn.close()

def get_all_messages():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    rows = c.fetchall()
    conn.close()
    return rows

@app.route('/api/message', methods=['POST'])
def handle_message():
    data = request.json  # Obtener los datos JSON de la solicitud POST

    # Verificar si se proporcionó la entidad "Message" en la solicitud
    if 'cmd' in data and 'hostname' in data and 'player' in data:
        cmd = data['cmd']
        hostname = data['hostname']
        player = data['player']
        team = player.get('team')
        home = player.get('home')
        from_value = player.get('from')

        # Insertar el mensaje en la base de datos
        insert_message(cmd, hostname, team, home, from_value)

        # Ejemplo de respuesta con un mensaje de éxito
        response = {
            'status': 'success',
            'message': f'Recibido comando: {cmd} para el host: {hostname}'
        }
        return jsonify(response), 200
    else:
        # En caso de que la entidad "Message" no esté completa en la solicitud
        response = {
            'status': 'error',
            'message': 'Entidad Message incompleta en la solicitud'
        }
        return jsonify(response), 400

@app.route('/api/message', methods=['GET'])
def get_message():
    # Obtener todos los mensajes de la base de datos
    messages = get_all_messages()

    # Crear una lista de diccionarios con los mensajes
    message_list = []
    for message in messages:
        cmd, hostname, team, home, from_value = message
        message_dict = {
            'cmd': cmd,
            'hostname': hostname,
            'player': {
                'team': team,
                'home': home,
                'from': from_value
            }
        }
        message_list.append(message_dict)

    # Respuesta con los mensajes en formato JSON
    response = {
        'status': 'success',
        'messages': message_list
    }
    return jsonify(response), 200

if __name__ == '__main__':
    create_table()
    app.run()
