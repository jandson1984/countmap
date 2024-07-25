import overpy

# Inicializa a API Overpass
api = overpy.Overpass()

# Define a consulta para obter os limites da área de Camocim
query_area = """
[out:json];
area["name"="Camocim"]["boundary"="administrative"];
out body;
"""

# Executa a consulta para obter os limites da área
result_area = api.query(query_area)

# Verifica se encontrou a área
if not result_area.areas:
    print("Não foi possível encontrar a área de Camocim.")
else:
    # Obtém o ID da área
    area_id = result_area.areas[0].id

    # Define a consulta para obter as ruas dentro dos limites de Camocim
    query_streets = f"""
    [out:json];
    area({area_id})->.searchArea;
    (
      way["highway"](area.searchArea);
    );
    out body;
    """

    # Executa a consulta para obter as ruas
    result_streets = api.query(query_streets)

    # Conta o número de ruas
    num_ruas = len(result_streets.ways)
    print(f"Número de ruas em Camocim: {num_ruas}")

    # Lista os nomes das ruas
    ruas = []
    for way in result_streets.ways:
        if "name" in way.tags:
            ruas.append(way.tags["name"])
    
    print(f"Nomes das ruas em Camocim: {ruas}")
