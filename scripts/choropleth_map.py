
import folium
import pandas as pd
import os

os.chdir('..')

states = os.path.join('geo_data','mexican_states.json')
precio_medio_rural_del_cafe_cereza_en_mexico = os.path.join('data','precio-medio-rural-del-cafe-cereza-en-mexico.csv')
state_data = pd.read_csv(precio_medio_rural_del_cafe_cereza_en_mexico)

# Map
m = folium.Map(location=[23.634501, -102.552784], zoom_start=5)

# States coordinates
agu = [22.021667, -102.356389]
bcn = [29.95, -115.116667]
bcs = [25.846111, -111.972778]
cam = [18.836389, -90.403333]
chp = [16.41, -92.408611]
chh = [28.814167, -106.439444]
cmx = [19.419444, -99.145556]
coa = [27.302222, -102.044722]
col = [19.096667, -103.960833]
dur = [24.934722, -104.911944]
gua = [21.018889, -101.262778]
gro = [17.613056, -99.95]
hid = [20.478333, -98.863611]
jal = [20.566667, -103.676389]
mex = [19.354167, -99.630833]
mic = [19.168611, -101.899722]
mor = [18.7475, -99.070278]
nay = [21.743889, -105.228333]
nle = [25.566667, -99.970556]
oax = [16.898056, -96.414167]
pue = [19.003611, -97.888333]
que = [20.591, -100.391]
roo = [19.6, -87.916667]
slp = [22.603333, -100.429722]
sin = [25.002778, -107.502778]
son = [29.646111, -110.868889]
tab = [17.972222, -92.588889]
tam = [24.287222, -98.563333]
tla = [19.428889, -98.160833]
ver = [19.434722, -96.383056]
yuc = [20.833333, -89]
zac = [23.292778, -102.700556]

precio = folium.features.Choropleth(
            geo_data=states,
            name='precio',
            data=state_data,
            columns=['State','1999'],
            key_on='feature.id',
            fill_color='Greens',
            nan_fill_color='none',
            fill_opacity=0.7,
            line_opacity=0.2,
            Highlight=True,
            show=True,
            legend_name='MXN por tonelada de café',
            )

m.add_child(precio)

folium.LayerControl().add_to(m)

os.chdir('html')
tooltip = 'Da clic!'

folium.Marker(chp, popup='CHP<br><iframe src="chiapas_fig.html" title="Gráfica de Datos - Chiapas" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(col, popup='COL<br><iframe src="colima_fig.html" title="Gráfica de Datos - Colima" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(gro, popup='GRO<br><iframe src="guerrero_fig.html" title="Gráfica de Datos - Guerrero" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(hid, popup='HID<br><iframe src="hidalgo_fig.html" title="Gráfica de Datos - Hidalgo" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(jal, popup='JAL<br><iframe src="jalisco_fig.html" title="Gráfica de Datos - Jalisco" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(mic, popup='MIC<br><iframe src="michoacan_fig.html" title="Gráfica de Datos - Michoacan" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(mor, popup='MOR<br><iframe src="morelos_fig.html" title="Gráfica de Datos - Morelos" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(nay, popup='NAY<br><iframe src="nayarit_fig.html" title="Gráfica de Datos - Nayarit" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(oax, popup='OAX<br><iframe src="oaxaca_fig.html" title="Gráfica de Datos - Oaxaca" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(pue, popup='PUE<br><iframe src="puebla_fig.html" title="Gráfica de Datos - Puebla" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(slp, popup='SLP<br><iframe src="san luis potosi_fig.html" title="Gráfica de Datos - San luis potosi" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(tab, popup='TAB<br><iframe src="tabasco_fig.html" title="Gráfica de Datos - Tabasco" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(ver, popup='VER<br><iframe src="veracruz_fig.html" title="Gráfica de Datos - Veracruz" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)



"""
# Markers
folium.Marker(agu, popup='AGU<br><iframe src="aguascalientes_fig.html" title="Gráfica de Datos - Aguascalientes" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(bcn, popup='BCN<br><iframe src="baja california_fig.html" title="Gráfica de Datos - Baja California" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(bcs, popup='BCS<br><iframe src="baja california_fig.html" title="Gráfica de Datos - Baja California Sur" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(cam, popup='CAM<br><iframe src="campeche_fig.html" title="Gráfica de Datos - Campeche" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(chp, popup='CHP<br><iframe src="chiapas_fig.html" title="Gráfica de Datos - Chiapas" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(chh, popup='CHH<br><iframe src="chihuahua_fig.html" title="Gráfica de Datos - Chihuahua" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(cmx, popup='CDMX<br><iframe src="distrito federal_fig.html" title="Gráfica de Datos - CDMX" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
folium.Marker(coa, popup='COA<br><iframe src="coahuila_fig.html" title="Gráfica de Datos - Coahuila" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(col, popup='COL<br><iframe src="colima_fig.html" title="Gráfica de Datos - Colima" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(dur, popup='DUR<br><iframe src="durango_fig.html" title="Gráfica de Datos - Durango" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(gua, popup='GUA<br><iframe src="guanajuato_fig.html" title="Gráfica de Datos - Durango" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(gro, popup='GRO<br><iframe src="guerrero_fig.html" title="Gráfica de Datos - Guerrero" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(hid, popup='HID<br><iframe src="hidalgo_fig.html" title="Gráfica de Datos - Hidalgo" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(jal, popup='JAL<br><iframe src="jalisco_fig.html" title="Gráfica de Datos - Jalisco" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(mex, popup='MEX<br><iframe src="mexico_fig.html" title="Gráfica de Datos - Mexico" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
folium.Marker(mic, popup='MIC<br><iframe src="michoacan_fig.html" title="Gráfica de Datos - Michoacan" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(mor, popup='MOR<br><iframe src="morelos_fig.html" title="Gráfica de Datos - Morelos" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(nay, popup='NAY<br><iframe src="nayarit_fig.html" title="Gráfica de Datos - Nayarit" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(nle, popup='NLE<br><iframe src="nuevo leon_fig.html" title="Gráfica de Datos - Nuevo leon" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(oax, popup='OAX<br><iframe src="oaxaca_fig.html" title="Gráfica de Datos - Oaxaca" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(pue, popup='PUE<br><iframe src="puebla_fig.html" title="Gráfica de Datos - Puebla" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(que, popup='QUE<br><iframe src="queretaro_fig.html" title="Gráfica de Datos - Queretaro" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(roo, popup='ROO<br><iframe src="quintana roo_fig.html" title="Gráfica de Datos - Quintana Roo" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(slp, popup='SLP<br><iframe src="san luis potosi_fig.html" title="Gráfica de Datos - San luis potosi" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(sin, popup='SIN<br><iframe src="sinaloa_fig.html" title="Gráfica de Datos - Sinaloa" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(son, popup='SON<br><iframe src="sonora_fig.html" title="Gráfica de Datos - Sonora" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(tab, popup='TAB<br><iframe src="tabasco_fig.html" title="Gráfica de Datos - Tabasco" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(tam, popup='TAM<br><iframe src="tamaulipas_fig.html" title="Gráfica de Datos - Tamaulipas" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(tla, popup='TLA<br><iframe src="tlaxcala_fig.html" title="Gráfica de Datos - Tlaxcala" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(ver, popup='VER<br><iframe src="veracruz_fig.html" title="Gráfica de Datos - Veracruz" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='darkred', icon='info-sign')).add_to(m)
folium.Marker(yuc, popup='YUC<br><iframe src="yucatan_fig.html" title="Gráfica de Datos - Yucatan" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
folium.Marker(zac, popup='ZAC<br><iframe src="zacatecas_fig.html" title="Gráfica de Datos - Zacatecas" width="840" height="530"></iframe>', tooltip=tooltip, icon=folium.Icon(color='lightred', icon='info-sign')).add_to(m)
"""


# Generate map
m.save('map_mex_choropleth.html')
