# Example CDP Infrastructure

Full infrastructure setup for whole system / integration level testing.

---

## Initial Comments
This is primarily used for developer stack creation and management.
We have an example stack, infrastructure, pipeline, and web app available for
demonstration and example data usage in our
[example repo](https://github.com/CouncilDataProject/example).

If you are just trying to process example CDP data (or for front-end: visualize example
CDP data) and not _upload_ data, it is recommended to simply point your requests at the
example stack.

---

## Dependencies

Deploying the CDP infrastructure requires having `cdp-backend` installed. Please see the
[project installation details](https://github.com/CouncilDataProject/cdp-backend#installation)
for more information.

## GCP Account Setup
* [Create or Sign-in to a Google Cloud account](https://console.cloud.google.com/)
* Once signed in, setup a [billing account](https://console.cloud.google.com/billing)

Additionally, you will need to
[create a GCP project](https://console.cloud.google.com/projectselector2/home/dashboard)
for the stack and all it's services to live in -- i.e. `cdp-dev-jackson-5`

Note: Try to use the same project and infrastructure as much as possible, there are
limits for how many projects and Firestore applications a single user can have.

## Environment Setup
The only environment setup needed to run this deployment is to make sure `pulumi` itself
and the `gcloud` SDK are both installed.

* [pulumi](https://www.pulumi.com/docs/get-started/install/)
* [gcloud](https://cloud.google.com/sdk/install)

_If this was the first time installing either of those packages, it is recommended to
restart your terminal after installation._

After `pulumi` and `gcloud` have both been installed and terminal restarted, run the
following commands to setup your local machine with credentials to both services.

1. `pulumi login`
2. `gcloud auth login`
3. `gcloud auth application-default login`

## Stack Initialization
To setup a new CDP Infrastructure stack run:

`pulumi stack init {gcp-project-id}`

And fill the `{gcp-project-id}` with the Id of the GCP project you created earlier.
_Note: The GCP Project Id isn't always the same as the GCP project name._

By default, the current `__main__.py` file used by `pulumi`, assumes the stack name
matches the GCP project id for the GCP project you want to deploy the infrastructure on.

## Deployment Process and Common Commands
* To create a new deployment or update an existing deployment, run: `pulumi up -p 5`
  * Note: the `-p 5` sets the maximum number of parallel resources that can be created
  at any one time, we do this to resolve Google's API limits.
* To delete an existing deployment, run: `pulumi destroy`
* To view all created and managed stacks, run: `pulumi stack ls`
* To switch to a different stack, run: `pulumi stack select {stack-name}`
* To completely destroy a stack and it's history, run: `pulumi stack rm {stack-name}`
  * Note: this doesn't not remove the GCP project and the infrastructure on it, just
  the Pulumi stack.

For a full list of `pulumi` CLI commands, see their
[documentation](https://www.pulumi.com/docs/reference/cli/)

## Non-Default Parameters

If you want to edit the default behavior of the `__main__.py` file and change the
parameters, please see the documentation for the
[CDPStack object](https://councildataproject.github.io/cdp-backend/cdp_backend.infrastructure.html#module-cdp_backend.infrastructure.cdp_stack)
