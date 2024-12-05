import webbrowser

def open_browser_tab(url=None):
    """
    Opens a new browser tab with the specified URL.

    Args:
        url (str): The URL to open in the browser.

    Returns:
        Opens browser tab
    """

    if url == None:
        url = "https://www.youtube.com/watch?v=N-FYySSy0rM" # Luuk's favourite song
        print("You are now listening to Luuk's favourite song :P")

    try:
        webbrowser.open_new_tab(url)
    except Exception as e:
        print(f"An error occurred: {e}")

