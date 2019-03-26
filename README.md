# salesforce-schema-viewer

A script of several lines that uses [simple-salesforce](https://github.com/simple-salesforce/simple-salesforce) to output a csv representation of the fields for an object. This can be used to easily see **and share** what fields are available along with the relevant details. 

* Generate a user token
* Update the `username`, `password`, `secutiy_token` and `{domain}`
* Replace the Account in `sf.Account.describe()["fields"]` with the relevant [sales object](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_erd_majors.htm) if required. 
