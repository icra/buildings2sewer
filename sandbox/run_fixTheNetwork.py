import processing

abs_path = 'C:/Users/jpueyo/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/QGISprocessing/algs/dataset/'

feedback = QgsProcessingFeedback()
params = {'ARCS': abs_path + 'AdG_arc_2021.gpkg|layername=arc',
          'NODES': abs_path + 'AdG_node_2021.gpkg|layername=node',
          'node_1': 'node_1',
          'node_2': 'node_2',
          'node_id': 'node_id',
          'wwtp': '32377',
          'DEM': abs_path + 'dem.tif',
          'FIXED_NODES': 'TEMPORARY_OUTPUT',
          'FIXED_ARCS': 'TEMPORARY_OUTPUT'
          }

processing.runAndLoadResults('ICRA:Fix the sewer network', params, feedback=feedback)
