import pandas as pd

def transform_orden_trabajo(df_mano_de_obra, df_materiales, df_orden_de_trabajo):
    mano_de_obra_agrupado = df_mano_de_obra.groupby('idorden_de_trabajo')['total'].sum().reset_index()
    materiales_agrupados = df_materiales.groupby('idorden_de_trabajo')['total'].sum().reset_index()
    df_orden_material = pd.merge(df_orden_de_trabajo[['idorden_de_trabajo','fecha_creacion','idvehiculo']], materiales_agrupados, on = 'idorden_de_trabajo', how='left')
    df_orden_material = df_orden_material.rename(columns={'total': 'costo_materiales'})
    df_orden_completo = pd.merge(df_orden_material, mano_de_obra_agrupado, on = 'idorden_de_trabajo', how='left')
    df_orden_completo = df_orden_completo.rename(columns={'total': 'costo_mano_obra'})
    df_orden_completo['fecha_creacion'] = pd.to_datetime(df_orden_completo['fecha_creacion'])
    df_orden_completo['dia_fecha_creacion'] = df_orden_completo['fecha_creacion'].dt.day
    df_orden_completo['mes_fecha_creacion'] = df_orden_completo['fecha_creacion'].dt.month
    df_orden_completo['año_fecha_creacion'] = df_orden_completo['fecha_creacion'].dt.year
    df_orden_completo['costo_materiales'] = df_orden_completo['costo_materiales'].fillna(0) * 4000
    df_orden_completo['costo_mano_obra'] = df_orden_completo['costo_mano_obra'].fillna(0) * 4000
    df_orden_completo['costo_total'] = df_orden_completo['costo_materiales'] + df_orden_completo['costo_mano_obra']
    return df_orden_completo

def transform_materiales(df_materiales, df_articulo):
    df_dimension_materiales = pd.merge(df_materiales, df_articulo[['idarticulo','descripcion']], on = 'idarticulo', how='left')
    df_dimension_materiales = df_dimension_materiales.rename(columns={'descripcion': 'descripcion_articulo', 'costo_total': 'total'})
    df_dimension_materiales['costo_unitario'] = df_dimension_materiales['costo_unitario'].fillna(0) * 4000
    df_dimension_materiales['total'] = df_dimension_materiales['total'].fillna(0) * 4000
    return df_dimension_materiales

def transform_materiales_mano_de_obra(df_mano_de_obra, df_mecanico):
    df_dimension_mano_de_obra = pd.merge(df_mano_de_obra, df_mecanico[['idmecanico','nombre','apellido']], on = 'idmecanico', how='left')
    df_dimension_mano_de_obra['nombre_completo'] = df_dimension_mano_de_obra['nombre'] + ' ' + df_dimension_mano_de_obra['apellido']
    df_dimension_mano_de_obra['costo_por_hora'] = df_dimension_mano_de_obra['costo_por_hora'].fillna(0) * 4000
    df_dimension_mano_de_obra['total'] = df_dimension_mano_de_obra['total'].fillna(0) * 4000
    return df_dimension_mano_de_obra

def transform_materiales_vehiculo(df_vehiculo):
    df_dimension_vehiculo = df_vehiculo.rename(columns = {'pais_matricula' : 'pais'}) 
    return df_dimension_vehiculo