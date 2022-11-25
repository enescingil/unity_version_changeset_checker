import os

versions =	{ '2022.1.0f1': '369b620af41c', '2022.1.1f1': '53d13f540f71',"2022.1.2f1": "9427c1534183","2022.1.3f1": "1cedbfe38737","2022.1.4f1": "76dd1f94b339","2022.1.5f1": "feea5ec8f162","2022.1.6f1": "e49a51cf6290","2022.1.7f1": "240f4c1f462c","2022.1.8f1": "2961e8c2b463","2022.1.9f1": "07e076b6d414","2022.1.10f1": "9aa0f82c4f96","2022.1.11f1": "09bebd6e9324","2022.1.12f1": "916d9c03b898","2022.1.13f1": "22856944e6d2","2022.1.14f1": "ff7e140968b4","2022.1.15f1": "42973686a05c","2022.1.16f1": "7321c9670bc2","2022.1.17f1": "2d349551e475","2022.1.18f1": "8a091f9adba4","2022.1.19f1": "2fd7b40534d1","2022.1.20f1": "01d83b40d570","2022.1.21f1": "9ac1ff5ca45b","2022.1.22f1": "6b6e9fc2adda","2022.1.23f1": "9636b062134a","2020.3.40f1": "ba48d4efcef1","2020.3.15f2": "6cf78cb77498","2020.3.41f1": "7c19dc9acfda"}

UNITY_VERSION = os.environ['UNITY_VERSION']
#print(UNITY_VERSION)

def main(version):
    UNITY_CHANGESET_VAR = versions[UNITY_VERSION]
    os.environ['UNITY_CHANGESET'] = UNITY_CHANGESET_VAR
    print(os.environ["UNITY_CHANGESET"])
    return UNITY_CHANGESET_VAR

if __name__ == "__main__":
    main(os.environ['UNITY_VERSION'])
