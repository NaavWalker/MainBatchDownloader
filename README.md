# MainBatchDownloader
Note: this requires that YT doesn't block you IP or similar, while the script is running. If the job breaks, you could perhaps start script again and YT-DLP will probably log "video X has already been downloaded" or similar.
But you could do xlookups and figure out where job broke and iterate over remainig IDs. See other repo for that script  ('...afterSplitOut')
Also, BEWARE that the script might ACTUALLY run in _another_ directory than where the .py file is located, then you either need to fix that, or just add YT-DLP.exe + 3 ffmpeg files to that dir. For instance, my script actually ran in evlo8 users dir, even though I changed, and I got some formatting error messages becuase it could not locate the ffmpeg files.
