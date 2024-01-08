from flask import Flask, request, jsonify
from clickhouse_driver import Client
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

client = Client(
    host=app.config['CLICKHOUSE_HOST'],
    port=app.config['CLICKHOUSE_PORT'],
    user=app.config['CLICKHOUSE_USER'],
    password=app.config['CLICKHOUSE_PASSWORD'],
    database=app.config['CLICKHOUSE_DATABASE']
)

# Пример запроса для выгрузки данных в активный канал (табличный вид)
@app.route('/api/data', methods=['GET'])
def get_data():
    query = """
    SELECT 
        seid AS SvrSeid, srt AS SvrSrt, seid, srt AS SRT, type, srt, name, 
        deviceAddress, deviceHostName, 
        transform(severity, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
        ['Very-Low', 'Very-Low', 'Very-Low', 'Low', 'Low', 'Medium', 'Medium', 
        'High', 'High', 'Very-High', 'Very-High'], 'Very-Low') AS severity, 
        destinationAddress, destinationUserName, sourceAddress, sourceUserName, 
        deviceVendor, deviceProduct, agentAddress 
    FROM savrus.data 
    WHERE 
        (srtd >= toDate(1694608894, 'GMT') AND srtd <= toDate(1695040868, 'GMT')) 
        AND srth >= (intDiv(1694608894, 3600) * 3600) 
        AND srth <= (intDiv(1695040868, 3600) * 3600) + 3600 
        AND srtm >= (intDiv(1694608894, 60) * 60) 
        AND srtm <= (intDiv(1695040868, 60) * 60) + 60 
        AND (srt >= 1694608894) 
        AND (srt <= 1695040868) 
    ORDER BY SvrSeid DESC 
    LIMIT 6494;
    """
    try:
        result = client.execute(query)
        columns = [column[0] for column in client.execute("DESCRIBE TABLE savrus.data")]
        data = [dict(zip(columns, row)) for row in result]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Пример запроса для построения радара 2
@app.route('/api/radar', methods=['GET'])
def get_radar_data():
    query = """
    SELECT 'Events' AS argument,  
        multiIf(
            (srt > (1695213669 - 25200)) AND (srt <= 1695213669), 24,
            (srt <= (1695213669 - 25200)) AND (srt > (1695213669 - 50400)), 23,
            (srt <= (1695213669 - 50400)) AND (srt > (1695213669 - 75600)), 22,
            (srt <= (1695213669 - 75600)) AND (srt > (1695213669 - 100800)), 21,
            (srt <= (1695213669 - 100800)) AND (srt > (1695213669 - 126000)), 20,
            (srt <= (1695213669 - 126000)) AND (srt > (1695213669 - 151200)), 19,
            (srt <= (1695213669 - 151200)) AND (srt > (1695213669 - 176400)), 18,
            (srt <= (1695213669 - 176400)) AND (srt > (1695213669 - 201600)), 17,
            (srt <= (1695213669 - 201600)) AND (srt > (1695213669 - 226800)), 16,
            (srt <= (1695213669 - 226800)) AND (srt > (1695213669 - 252000)), 15,
            (srt <= (1695213669 - 252000)) AND (srt > (1695213669 - 277200)), 14,
            (srt <= (1695213669 - 277200)) AND (srt > (1695213669 - 302400)), 13,
            (srt <= (1695213669 - 302400)) AND (srt > (1695213669 - 327600)), 12,
            (srt <= (1695213669 - 327600)) AND (srt > (1695213669 - 352800)), 11,
            (srt <= (1695213669 - 352800)) AND (srt > (1695213669 - 378000)), 10,
            (srt <= (1695213669 - 378000)) AND (srt > (1695213669 - 403200)), 9,
            (srt <= (1695213669 - 403200)) AND (srt > (1695213669 - 428400)), 8,
            (srt <= (1695213669 - 428400)) AND (srt > (1695213669 - 453600)), 7,
            (srt <= (1695213669 - 453600)) AND (srt > (1695213669 - 478800)), 6,
            (srt <= (1695213669 - 478800)) AND (srt > (1695213669 - 504000)), 5,
            (srt <= (1695213669 - 504000)) AND (srt > (1695213669 - 529200)), 4,
            (srt <= (1695213669 - 529200)) AND (srt > (1695213669 - 554400)), 3,
            (srt <= (1695213669 - 554400)) AND (srt > (1695213669 - 579600)), 2,
            (srt <= (1695213669 - 579600)) AND (srt >= 1694608869), 1, 
            NULL
        ) AS number, 
        max(srt), min(srt), 
        count(argument) AS cnt 
    FROM savrus.data  
    WHERE 
        (srtd >= toDate(1694608869, 'GMT') AND srtd <= toDate(1695213669, 'GMT')) 
        AND srth >= (intDiv(1694608869, 3600) * 3600) 
        AND srth <= (intDiv(1695213669, 3600) * 3600) + 3600  
        AND srtm >= (intDiv(1694608869, 60) * 60) 
        AND srtm <= (intDiv(1695213669, 60) * 60) + 60  
        AND (srt >= 1694608869) 
        AND (srt <= 1695213669) 
    GROUP BY number, argument;
    """
    try:
        result = client.execute(query)
        columns = [column[0] for column in client.execute("DESCRIBE TABLE savrus.data")]
        radar_data = [dict(zip(columns, row)) for row in result]
        return jsonify(radar_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Пример запроса диаграммы (
# попробовать пирог, 
# гистограмму (с разрывами желательно, чтобы на одной диаграмме можно было разномасштабные колонки показать), 
# табличное отображение)
@app.route('/api/pie_chart', methods=['GET'])
def get_pie_chart_data():
    query = """
    SELECT destinationAddress, SUM(cnt) 
    FROM (
        SELECT destinationAddress, COUNT(destinationAddress) AS cnt 
        FROM savrus.data 
        WHERE srtd >= '2023-09-12' AND srtd <= '2023-09-20' 
        AND (srt >= 1694608869) AND (srt <= 1695213669) 
        AND NOT EMPTY(TOSTRING(destinationAddress)) 
        GROUP BY destinationAddress
    ) 
    GROUP BY destinationAddress 
    ORDER BY SUM(cnt) DESC;
    """
    try:
        result = client.execute(query)
        columns = [column[0] for column in client.execute("DESCRIBE TABLE savrus.data")]
        pie_chart_data = [dict(zip(columns, row)) for row in result]
        return jsonify
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Пример запроса диаграммы 4
@app.route('/api/bar_chart', methods=['GET'])
def get_bar_chart_data():
    query = """
    SELECT destinationUserName, SUM(cnt) 
    FROM (
        SELECT destinationUserName, COUNT(destinationUserName) AS cnt 
        FROM savrus.data 
        WHERE srtd >= '2023-09-12' AND srtd <= '2023-09-20' 
        AND (srt >= 1694608869) AND (srt <= 1695213669) 
        AND NOT EMPTY(TOSTRING(destinationUserName)) 
        GROUP BY destinationUserName
    ) 
    GROUP BY destinationUserName 
    ORDER BY SUM(cnt) DESC;
    """
    try:
        result = db.session.execute(query)
        bar_chart_data = [dict(row) for row in result]
        return jsonify(bar_chart_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/query', methods=['POST'])
def execute_query():
    query = request.json.get('query')
    try:
        result = db.session.execute(query)
        data = [dict(row) for row in result]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
