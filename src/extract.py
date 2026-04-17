def extract_data(endpoint: str = "/users", params: dict | None = None) -> list[dict]:
    """Extrae datos de la API REST con manejo de errores básicos."""
    url = f"{API_BASE_URL}{endpoint}"
    headers = build_headers()
    
    logger.info(f"Iniciando extracción desde: {url}")
    
    try:
        # Enviamos la petición GET con un tiempo de espera de seguridad
        response = requests.get(url, headers=headers, params=params, timeout=(5, 30))
        
        # Lanza una excepción si el código es 4xx o 5xx [cite: 358, 448]
        response.raise_for_status() 
        
        # Convertimos la respuesta JSON a una lista de diccionarios Python [cite: 453, 455]
        data = response.json()
        
        # Lógica para extraer la lista de registros (maneja si viene en un 'wrapper') [cite: 460, 465]
        records = data if isinstance(data, list) else data.get("results", [data])
        
        logger.info(f"Extracción exitosa: {len(records)} registros.")
        return records

    except requests.exceptions.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else "?"
        logger.error(f"Error HTTP {status}: {exc}")
        raise # Re-lanzamos para que el orquestador sepa que falló
