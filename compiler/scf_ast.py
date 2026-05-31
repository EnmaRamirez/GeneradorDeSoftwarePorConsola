from grammar.generated.GenSoftParser import GenSoftParser


def build_project_spec(arbol):
    """Convierte el árbol ANTLR a datos estructurados del proyecto."""
    proyectos = []
    generar = []

    for sentencia in arbol.sentencia():
        if sentencia.declaracionProyecto():
            proyectos.append(_parse_proyecto(sentencia.declaracionProyecto()))
        elif sentencia.comandoGenerar():
            generar.append(sentencia.comandoGenerar().ID().getText())

    return {
        "projects": proyectos,
        "generate": generar,
    }


def _parse_proyecto(ctx: GenSoftParser.DeclaracionProyectoContext):
    return {
        "name": ctx.ID().getText(),
        "project_type": ctx.tipoProyecto().getText(),
        "modules": [_parse_modulo(modulo) for modulo in ctx.modulo()],
    }


def _parse_modulo(ctx: GenSoftParser.ModuloContext):
    return {
        "name": ctx.ID().getText(),
        "fields": [_parse_campo(campo) for campo in ctx.campo()],
    }


def _parse_campo(ctx: GenSoftParser.CampoContext):
    return {
        "name": ctx.ID().getText(),
        "type": ctx.tipoDato().getText(),
    }
