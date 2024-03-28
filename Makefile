
SERVICE_NAME=MojStack-$(ENV)

read_env:
	python -c "from util import *; read_env('$(ENV)')"

deploy:
	cdk deploy $(SERVICE_NAME)

destroy:
	cdk destroy $(SERVICE_NAME)

#deploy:
#	$(MAKE) read_env
#	python -c "import os; print('${API_PREFIX}')"

print:
	python -c "from cdk.cdk_stage_1_stack import CdkStage1Stack, get_stack_name"
	python -c "print('$(get_stack_name())')"
	#python -c "print('$(SERVICE_NAME)')"


