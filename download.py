import requests, os

folder = input('Enter Folder: ')
dir_path = os.path.join(os.getcwd() + '\downloads', folder)

name = 'Evil'
season = 1

try:
    os.mkdir(dir_path)
except Exception as err:
    print(err)
finally:

    begin = 1
    end = 12
    for i in range(begin, end + 1):

        url = f"http://d8.o2tv.org/Sleepy%20Hollow/Season%2004/Sleepy%20Hollow%20-%20S04E{0 if i < 10 else ''}{i}%20HD%20(TvShows4Mobile.Com).mp4"
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(dir_path, f"{name} - S0{season}E0{i}.mp4"), 'wb') as file:
                print(f'Downloading: {name} - S0{season}E0{i}.mp4', )
                for packet in response.iter_content(chunk_size=1024):
                    file.write(packet)
        else:
            print(url)
            print('Problem Dey. E no connect')
            break
