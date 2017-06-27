//Base64 Remover - This will remove non base64 characters and decode.
var changeme = ';UEsDBBQAAAAIAOCIr0qMVwGeKQAAACoA<AAAIABwAZmlsZS5kYXRVVAkAA3QYGlmB=GBpZdXgLAAEE6AMAAAToAwAAC3D0q3bM:yQnIz8wrSS0q9sxz8QsOzsgvzUkBCzkl>JmeXJxalFNdyAQBQSwECHgMUAAAACADg:iK9KjFcBnikAAAAqAAAACAAYAAAAAAAB$-=7AAAAtIEAAAAAZmlsZS5kYXRVVAUAA3QY;Gll1eAsAAQToAwAABOgDAABQSwUGAAAA/AAEAAQBOAAAAawAAAAAA'
	changeme = changeme.replace(/[^A-Za-z0-9\+\/\=]/g, '');
console.log('\n' + ' + + + Formatted Base64 below + + +' + '\n\n' + changeme + '\n')
var decoded = new Buffer(changeme, 'base64').toString('ascii')
console.log('\n' + '+ + + Base64 Decoded content below + + +' +'\n\n' + decoded)