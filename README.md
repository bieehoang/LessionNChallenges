# README #
## Setup
* DEV *
- Install mongodb 
- Install npm version 14. 

## Steps:
Setup project
Linux:
- Step 1: Install packages && reconfig
	- Checkout, pull from master to branch feature/bdstraining
	- Diagram: API( server ), cms( Admin manage ), www( User view)
	- install packages ( Api, www, cms )/package.json
	- Reconfig for development ( Api, www )/config.js {
		reactpress.local:port => localhost:port 
		# instance {
			const WebConfig = {
 				 development: {
 				   api: 'http://localhost:5102',
 				   image: 'http://localhost:5102/data/upload/images/',
 				   itemPerPage: 10,
 				   database: 'bds',
 				   web: 'http://localhost:5103',
 				   admin: 'http://localhost:5101',
 				   // api: 'https://codeapi.bacs.vn',
 				   // image: 'https://codeapi.bacs.vn/data/images/',
 				   // itemPerPage: 50,
 				   // database: 'codebacs'
 				 },
 				 production: {
 				   api: 'https://api.bdstraining.vn',
 				   image: 'https://api.bdstraining.vn/data/upload/images/',
 				   web: 'https://bdstraining.vn',
 				   admin: 'https://admin.bdstraining.vn',
 				   itemPerPage: 50,
 				   database: 'codebacs'
 				 }
			};
	}	
	- With cms { 
		#with froala third_party error  
		copy file www/pages/public/css/iconmins.min.css > cms/source/plugins/froala/css/third_party/
		copy file www/pages/public/css/reactpress.min.css > cms/source/plugins/froala/js/third_party/
	}
- Step 2: Run product
	* DIR: .../reactpress/
	- Restore mongodb: mongorestore -db namedb DIR/prod_backup/backup/bds
	- Run server: 
	cd Code/api && npm run dev 
	- Run UI/Website:
	change directory to www && npm run dev
	- Run Admin Site:
	cd Code/cms && npm run start ( For Windows )
	cd Code/cms && npm run ustart ( For Linux )

