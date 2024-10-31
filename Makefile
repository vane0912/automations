run_flask:
	flask --app automations run --debug
video:
	ffmpeg -framerate 1 -i automations/Applications/saved_screenshots/Correct/screenshot_%d.png -vcodec libx264 -pix_fmt yuv420p output.mp4
	rm automations/Applications/saved_screenshots/Correct/*
delete_images:
	rm automations/Applications/saved_screenshots/Correct/*