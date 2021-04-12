# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "BeyondInsight" + os.sep + "libs" + os.sep
sys.path.append(cur_path)
"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

global base_api, session

if module == "setCredentials":
    api_key = GetParams("api_key")
    run_as = GetParams("run_as")
    server = GetParams("server")
    try:
        base_api = "https://{server}/BeyondTrust/api/public/v3".format(server=server)
        header_params = "PS-Authkey={api_key};runas={run_as};".format(api_key=api_key, run_as=run_as)
        header={'Authorization': header_params}
        session = requests.Session()
        session.headers.update(header)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "getPasswords":
    import json
    result = GetParams("result")
    try:
        api_url = api_client.host
        response = session.post("base_api" + "/Auth/SignAppin")
        data = response.json()
        SetVar(result, data)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e
