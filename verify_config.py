from pathlib import Path
import json,yaml
r=Path(__file__).parent
c=yaml.safe_load((r/'docker-compose.yml').read_text())
assert set(c['services'])=={'mediamtx','mosquitto','nodered'}
assert all(str(port).startswith('127.0.0.1:') for v in c['services'].values() for port in v.get('ports',[]) if 'udp' not in str(port))
n=json.loads((r/'node-red-flow.json').read_text());ids={x['id'] for x in n}
assert any(x['type']=='rbe' for x in n)
assert any(x.get('topic')=='campus/raatbek/cam1/motion' for x in n)
assert all(id in ids for x in n for grp in x.get('wires',[]) for id in grp)
print('PASS config: 3 services, local ports, complete flow wiring, RBE')
