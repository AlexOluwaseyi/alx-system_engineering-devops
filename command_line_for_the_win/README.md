COMMAND LINE FOR THE WIN

This is an optional project on
ALX SOFTWARE ENGINEERING (ALXSWE) Programme

SFTP - Secure File Transfer Protocol

Steps:
1. 	Open cmd on Windows and typed "sftp user@remote_host_address".
2. 	Hit enter to initiate connection.
3. 	Enter remote_host password to authenticate connection.
4. 	Connection successful.
5. 	Confirm local working directory and remote working directories using
   	"lpwd" and "pwd" respectively.
6. 	Changed local working directory to where screenshots are saved.
	lcd "C:/Users/Owner/Pictures/Screenshots/ALX"
7.	Changed remote working directory to alx-system_engineering-devops directory
	cd "root/alx-system_engineering-devops"
8. 	Make remote directory in current remote working directory
	mkdir command_line_for_the_win
9.	Changed remote working directory to newly created directory
	cd command_line_for_the_win
10.	Checked local working drectory to confirm screenshots are available
	lls
11.	Put local files in current local working directory to current remote working directory using "put"
	put 0-first_9_tasks.png
	put 1-next_9_tasks.png
	put 2-next_9_tasks.png
12. 	List files in remote working directory to confim uploads
	ls
13. 	End secure connection to server
	quit
