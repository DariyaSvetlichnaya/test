from api_service.base_api import BaseApi


class VpnApi:

    api_executor = BaseApi()
    base_url = "https://rmzq829cg3.execute-api.us-east-1.amazonaws.com/sbx/api"
    all_users_url = f"{base_url}/v1/customers/200000/scanners/EXPR200009CT/vpn-hubs"

    token = {'Authorization': 'Bearer eyJraWQiOiJzXC83Q3lJTWhIRGFHZVFWaFM4QjhKZVhGdmJTSElVUWVieWdQOGVUaGltWT0iLCJhbGciOiJSUzI1NiJ9.eyJjdXN0b206dHlwZSI6ImFkbWluIiwic3ViIjoiMWY2NDhhYWItNDI2NS00NmIwLTk2MjEtYWFlMzZiNjRkYTQxIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX0NLZ0VYVmc2UyIsInBob25lX251bWJlcl92ZXJpZmllZCI6ZmFsc2UsImNvZ25pdG86dXNlcm5hbWUiOiJkc3ZpdGx5Y2huYS1sY2ciLCJhdWQiOiI2NTZmcDJtMDJwdnMzajRiMzFvc280cmNucCIsImN1c3RvbTppc19mZWRlcmF0ZWQiOiIwIiwiaWRlbnRpdGllcyI6W3sidXNlcklkIjoiZHN2aXRseWNobmFAZXZvbHZ0ZWNobm9sb2d5LmNvbSIsInByb3ZpZGVyTmFtZSI6ImV2b2x2dGVjaG5vbG9neS5jb20iLCJwcm92aWRlclR5cGUiOiJTQU1MIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoiZmFsc2UiLCJkYXRlQ3JlYXRlZCI6IjE3MDU0ODg5OTM2ODAifSx7InVzZXJJZCI6Im9rdGF8TXlFdm9sdi1DSUMtRGV2ZWxvcG1lbnR8MDB1M3N2MGJvcDhIb0lud1U2OTciLCJwcm92aWRlck5hbWUiOiJhdXRoMC1vcGVuaWQiLCJwcm92aWRlclR5cGUiOiJPSURDIiwiaXNzdWVyIjpudWxsLCJwcmltYXJ5IjoiZmFsc2UiLCJkYXRlQ3JlYXRlZCI6IjE3MDk4MzA2NzgwMTEifV0sImV2ZW50X2lkIjoiMDY3M2U0YzEtNDY1Ni00MWQzLThlOGQtOGRhZGNlYTRiOWM2IiwidG9rZW5fdXNlIjoiaWQiLCJjdXN0b206dGFibGVhdV91c2VyIjoiZHN2aXRseWNobmEtbGNnIiwiYXV0aF90aW1lIjoxNzExNjM1NTA2LCJleHAiOjE3MTE2MzU4MDYsImlhdCI6MTcxMTYzNTUwNiwiZW1haWwiOiJkc3ZpdGx5Y2huYUBldm9sdnRlY2hub2xvZ3kuY29tIn0.gyxa72O4UdQvIay1lMD1jcCxV-tjr8J0gZJivPOB2FAkzA127bxSp1oD60mYyGpD5suqsVokhQBEbyf4RtXXrWFAxLDpqyun8QtL7MZvhW9JC79wbNDkV7e8l2yEa-Xee3AU3o3VxfkbTCxNd-v4p8O9IfuI-PtHcAdbFGhuYLfJn1RaD42b3epXjU4JKhRdhRyf7OGD0LuApRxFYifZDcMdXJ6gFqCGN8o4FRy8lQT6ul73L-m6gBu0DCF-2mCT1BvyGiERpj5mmaxBLzCXOUsV9fVqnoBenaAv6Zh7yyzh66-XIzo-p5X5WHnxOdSVRHY5_fJvIbWX3AXsyQXm6w'}

    def get_vpn_hubs(self):

        return self.api_executor.get(url=self.all_users_url)

