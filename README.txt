Set Frame Range OTL

1. This tool checks the data from a notion table (you will need your notion_token and notion_page_id from notion), to get these go check https://developers.notion.com/reference/create-a-token and https://www.notion.so/help/unique-id
2. Run GetdatafromNotion.py to download the requiered information into a .json file
3. It will create 3 different .json files. 
	- db_info.json will have the database object information ( more information https://developers.notion.com/reference/retrieve-a-database )
	- db_rows.json will get the list of pages ( more information https://developers.notion.com/reference/post-database-query )
	- simple_rows.json is the cleaned information and the file that we will use to read the information inside houdini
4. After cleaning up the data paste the otls folder in your houdini folder usually located on C:\Users\Documents\houdini19.5
5. Inside the otl you will have the chance to search for the json path and by pressing Set the frame range will adjust depending on the Scene File name
