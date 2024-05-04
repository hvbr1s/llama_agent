## How to run the bot locally for testing purposes  

1. Make sure you have the correct `.env` variables: `OPENAI_API_KEY`, `BACKEND_API_KEY`, `API_KEY_NAME`, `PINECONE_API_KEY`, `PINECONE_ENVIRONMENT`
2. From the root folder, run `uvicorn app:app --reload --port 8800` to start a local instance of the bot 
3. Using Postman ping the `http://127.0.0.1:8800/gpt` endpoint with a request formatted as follow:

```
POST /gpt HTTP/1.1
Host: http://127.0.0.1:8800/gpt
Authorization: Bearer <BACKEND_API_KEY>
Content-Type: application/json

{
    "user_input": "your_question",
    "user_locale": "your_locale",
    "user_id": "any_number"
}
```
4.  After a brief moment (10-20 seconds), you should see the bot's response to your question appear in the console. You can test different locales by changing `user_locale` to `eng`, `fr`, etc.

# Versioned deployment

Pushing new code to the main branch will not automatically deploy a new version. You first need to create a new release with a unique version number then edit the `value.yaml` files for the STG or PRD deployment to create a new deployment on ArgoCD.

It's strongly recommended to deploy and test things out on STG before deploying new code to PRD. Once you're happy with your testing, follow the instructions to deploy a new version to PRD.

## How to deploy a new STG version

1. Push new code to the `main` branch via a PR and wait for it to be checked and deployed.
2. In Github, navigate to `Releases > Draft a new release`. Give your release a unique version number, a title and a description then click `Public release`.
3. Importantly, make sure to set your new release as the `latest release` and not as a `pre-release` by ticking the appropriate box on Github.
4. Once the release is created, open the `values.yaml` file located in `argocd/stg/` (make sure you're looking at the `stg` file and not the `prd` file)
5. In the `values.yaml` file, go to `tag` and change the version number. For example `v2.5.2` to `v2.5.3`.
6. This will open a PR which you need to merge. This PR should only contain the modified STG `values.yaml` file.
7. After merging the PR, open ArgoCD, navigate to the STG deployment of `knowledge_bot` and click on the `Refresh` button to start the deployment
8. Once the new image is deployed, test the STG changes thoroughly before deploying the new version to PRD.


## How to deploy a new PRD version

/!\ Again, it's strongly recommended to test things out on STG before deploying new code to PRD. Once you're happy with your testing, follow these instructions to deploy a new version to PRD.

1. Open the `values.yaml` file located in `argocd/prd/` (make sure you're looking at the `prd` file and not the `stg` file)
2. Go to `tag` and change the version number so it aligns with the STG release previously deployed. For example `v2.5.2` to `v2.5.3`.
3. This will open a PR which you need to merge. This PR should only contain the modified the PRD `values.yaml` file.
4. After merging the PR, open ArgoCD, navigate to the PRD deployment of `knowledge_bot`, and click on the `Refresh` button to start the deployment.
5. Monitor the logs carefully to make sure the deployment is successful and the app is receiving traffic.

Congratulations, you've successfully deployed your code to PRD!
