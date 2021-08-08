from botocore.exceptions import ClientError
import logging
import boto3
import requests
import tempfile
import urllib.request
from tqdm import tqdm


class FileUploader:

    def get_sprites(self, *args):
        if len(args) > 2:
            raise ValueError('Please, enter 1 or 2 integers')
        elif len(args) == 2:
            x = args[0]
            y = args[1]
        elif len(args) == 1:
            x = 1
            y = args[0]
        else:
            raise ValueError('Please, enter 1 or 2 integers')

        with tempfile.TemporaryDirectory() as temp_dir:
            for i in tqdm(range(x, y + 1)):

                r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')

                name = r.json()['name']
                back = r.json()['sprites']['back_default']
                front = r.json()['sprites']['front_default']

                urllib.request.urlretrieve(back, f'{temp_dir}/back.png')
                self.upload_file(f'{temp_dir}/back.png',
                                 'pokemon-sprites',
                                 f'{name}/back.png')

                urllib.request.urlretrieve(front, f'{temp_dir}/front.png')
                self.upload_file(f'{temp_dir}/front.png',
                                 'pokemon-sprites',
                                 f'{name}/front.png')

    def upload_file(self, file_name, bucket, object_name=None):
        """
        Upload a file to an S3 bucket

        Parameters
        ----------
        file_name : str
            Name of the file we want to upload
        bucket: str
            Name of the bucket
        object_name:
            Name of the object as we want it to appear in the bucket

        Returns
        -------
        bool
            False if the upload caused an error. True otherwise
        """
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True


if __name__ == '__main__':
    uploader = FileUploader()
    uploader.get_sprites(151, 200)
