import pandas as pd
import urllib.request

NAME_LIST = ["Black-naped Oriole", "Brown-throated Sunbird", "Collared Kingfisher",
            "Javan Myna", "Olive-backed Sunbird", "Pink-necked Green Pigeon", "Spotted Dove",
            "Striated Heron", "White-breasted Waterhen", "Yellow-vented Bulbul"]
    
def save_sampled_rows(name: str, data: pd.DataFrame):
    data.to_csv("./SampledData/" + name + ".csv")

def sample_data(url):
    data = pd.read_csv(url)
    filtered_data = data.loc[data['license'].str.len() > 0]
    sampled_data = filtered_data.sample(120).reset_index()
    return sampled_data

def download_image(url, file_path, file_name):
    full_path = file_path + file_name + '.png'
    urllib.request.urlretrieve(url, filename= full_path)

def download_images(urls, folder_name):
    for i in range(urls.shape[0]):
        download_image(urls[i], "images/" + folder_name + "/", folder_name + "-" + str(i))

def main():
    for name in NAME_LIST:
        sampled_data = sample_data("./data/" + name + ".csv")
        save_sampled_rows(name, sampled_data)
        download_images(sampled_data["image_url"], name)
        
main()
