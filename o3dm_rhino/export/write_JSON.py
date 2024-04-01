def write_JSON(file_path, data, sort_keys=True):
	import io
	import json
	with io.open(file_path, 'w', encoding='utf-8') as f:
		f.write(unicode(json.dumps(data, ensure_ascii=False, sort_keys=sort_keys, indent=4)))