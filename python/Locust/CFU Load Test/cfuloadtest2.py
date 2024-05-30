from locust import HttpUser, task, between
import json
from datetime import datetime

class GraphQLUser(HttpUser):
    host = "https://cfu-gateway.wlink.com.np"
    wait_time = between(1, 5)

    # Load tokens from the JSON file
    def load_tokens(file_path):
        with open(file_path, 'r') as file:
            tokens = json.load(file)
        return tokens

    def getTimeStamp(message, statuscode):
        print(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"), message, statuscode)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tokens = GraphQLUser.load_tokens('tokens.json')  # JSON file path
        self.token_index = 0

    def get_next_token(self):
        token = self.tokens[self.token_index]
        self.token_index = (self.token_index + 1) % len(self.tokens)
        return token

    @task
    def user(self): #1
        query = """
        {
          me {
            username
          }
        }
        """
        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query}, headers=headers, name="UserAPI")
        GraphQLUser.getTimeStamp("Response of user", response.status_code)
        print(response.text)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def load_disable(self): #2
        query = """
        query ($from: Int, $to: Int!, $supportzone_id: Int!, $filter: createFollowUpPayloadByUsernameWithExtraFilter) {
          loadDisabledCustomersByRange(from: $from, to: $to, supportzone_id: $supportzone_id, filter: $filter) {
            new_records {
              user_name
              plan_category_id
              plan_name
              usage_charge
              renew_date
              grace_status
              down_bw
              max_days
              client_name
              address
              contact_number
              email
              days_remaining
              balance
              support_zone
              disabled_days
              networktype
              onu_type
              onu_port
              olt_name
              nettv
              marketed_by
              auto_sync_date
              is_first_payment
              __typename
            }
            existing_records {
              user_name
              plan_category_id
              plan_name
              usage_charge
              renew_date
              grace_status
              down_bw
              max_days
              client_name
              address
              contact_number
              email
              days_remaining
              balance
              support_zone
              disabled_days
              networktype
              onu_type
              onu_port
              olt_name
              nettv
              marketed_by
              existing_created_at
              existing_updated_at
              existing_id
              existing_username
              existing_status
              existing_days_remaining
              existing_transfer_from_proactive
              existing_unique_identifier
              is_first_payment
              __typename
            }
            followUpTeam {
              id
              username
              branch
              status
              is_admin
              work_tag
              __typename
            }
            __typename
          }
        }
        """
        variables = {
            "from": -1,
            "to": -5,
            "supportzone_id": 39,
            "filter": {}
        }

        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='LoadDisable API')
        GraphQLUser.getTimeStamp("Response of Load Disable", response.status_code)
        print(response.text)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def load_proactive(self): #3
        query = """
        query ($supportzone_id: Int!, $from: Int, $to: Int!, $filter: createFollowUpPayloadByUsernameWithExtraFilter) {
          loadActiveCustomersByRange(supportzone_id: $supportzone_id, from: $from, to: $to, filter: $filter) {
            new_records {
              user_name
              plan_category_id
              plan_name
              create_date
              renew_date
              max_days
              contact_number
              client_name
              address
              phone
              balance
              support_zone
              expiry_date
              networktype
              days_remaining
              olt_name
              nettv
              marketed_by
              auto_sync_date
              down_bw
              grace_status
              disabled_days
              onu_type
              onu_port
              is_first_payment
              __typename
            }
            existing_records {
              user_name
              plan_category_id
              plan_name
              renew_date
              grace_status
              down_bw
              max_days
              client_name
              address
              contact_number
              balance
              support_zone
              days_remaining
              disabled_days
              networktype
              onu_type
              onu_port
              olt_name
              nettv
              marketed_by
              existing_id
              existing_username
              existing_status
              existing_days_remaining
              existing_transfer_from_proactive
              existing_created_at
              existing_updated_at
              existing_unique_identifier
              is_first_payment
              __typename
            }
            followUpTeam {
              id
              username
              status
              is_admin
              work_tag
              __typename
            }
            __typename
          }
        }
        """
        variables = {
            "from": 1,
            "to": 5,
            "supportzone_id": 38,
            "filter": {},
            "is_first_payment": "n"
        }

        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='LoadProactive API')
        GraphQLUser.getTimeStamp("Response of ProActive", response.status_code)
        print(response.text)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def courtesy_follow_up(self): #4
        query = """
        query ($from: Int, $to: Int!, $supportzone_id: Int!, $filter: createFollowUpPayloadByUsernameWithExtraFilter) {
          loadDisabledCustomersByRange(from: $from, to: $to, supportzone_id: $supportzone_id, filter: $filter) {
            new_records {
              user_name
              plan_category_id
              plan_name
              usage_charge
              renew_date
              grace_status
              down_bw
              max_days
              client_name
              address
              contact_number
              email
              days_remaining
              balance
              support_zone
              disabled_days
              networktype
              onu_type
              onu_port
              olt_name
              nettv
              marketed_by
              auto_sync_date
              is_first_payment
              __typename
            }
            existing_records {
              user_name
              plan_category_id
              plan_name
              usage_charge
              renew_date
              grace_status
              down_bw
              max_days
              client_name
              address
              contact_number
              email
              days_remaining
              balance
              support_zone
              disabled_days
              networktype
              onu_type
              onu_port
              olt_name
              nettv
              marketed_by
              existing_created_at
              existing_updated_at
              existing_id
              existing_username
              existing_status
              existing_days_remaining
              existing_transfer_from_proactive
              existing_unique_identifier
              is_first_payment
              __typename
            }
            followUpTeam {
              id
              username
              branch
              status
              is_admin
              work_tag
              __typename
            }
            __typename
          }
        }
        """
        variables = {
            "from": -1,
            "to": -5,
            "supportzone_id": 38,
            "filter": {},
            "is_first_payment": "n"
        }

        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='CourtesyFollowUp API')
        GraphQLUser.getTimeStamp("Response of CourtesyFollowUp", response.status_code)
        print(response.text)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def beacon_trial(self): #5
        query = """
        query ($supportzone_id: Int!, $filter: createFollowUpPayloadByUsernameWithExtraFilter) {
            loadTrialCustomersByRange(supportzone_id: $supportzone_id, filter: $filter) {
                new_records {
                username: user_name
                plan_category_id
                plan_name
                create_date
                disabledate: renew_date
                max_days
                mobile: contact_number
                name: client_name
                address
                phone
                balance
                support_zone
                expiry_date
                networktype
                days_remaining
                olt_name
                using_nettv: nettv
                marketed_by
                auto_sync_date
                down_bw
                grace_status
                disabled_days
                onu_type
                onu_port
                is_first_payment
                __typename
                }
                existing_records {
                user_name
                plan_category_id
                plan_name
                disabledate: renew_date
                grace_status
                down_bw
                max_days
                name: client_name
                address
                mobile: contact_number
                balance
                support_zone
                days_remaining
                disabled_days
                networktype
                onu_type
                onu_port
                olt_name
                using_nettv: nettv
                marketed_by
                existing_id
                existing_username
                status: existing_status
                existing_days_remaining
                existing_transfer_from_proactive
                loaded_date: existing_created_at
                followedDate: existing_updated_at
                existing_unique_identifier
                is_first_payment
                __typename
                }
                followUpTeam {
                id
                username
                status
                is_admin
                work_tag
                __typename
                }
                __typename
            }
        }
        """
        variables = {
            "supportzone_id": 38,
            "filter": {},
            "is_first_payment": "n"
        }

        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='BeaconTrial API')
        GraphQLUser.getTimeStamp("Response of BeaconTrial", response.status_code)
        print(response.text)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task()
    def dashboardapi1(self): #6
        query = """
        query ($region_id: [Int], $branch_id: [Int]) {
            ActiveCustomerCounts(region_id: $region_id, branch_id: $branch_id) {
            active_customers
            __typename
        }
      }
      """
        variables = {
        "region_id": [],
        "branch_id": []
      }
        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='ActiveCustomerCounts')
        GraphQLUser.getTimeStamp("Response of DashboardAPI1", response.status_code)
        print(response.text)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def clientlist(self): #7
        query = """
        query ($filter: userBranchQuery) {
          userByBranch(filter: $filter) {
            id
            username
            activityStatus
            name
            photo_link
            gender
            branches {
              branch_id
              userid
              __typename
            }
            work_tag
            count_assigned_clients
            __typename
          }
        }
"""
        variables = {
        "filter":
        {
        "branch": 26,
        "status": "y"
        }
      }
        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='ClientList')
        GraphQLUser.getTimeStamp("Response of ClientList", response.status_code)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")
    @task
    def goal_date(self):#8
        query = """
        query($goal_date:Date!){
  me {
      id
      username
      branches{
        branch_id,
        userid
      }
      goal(goal_date:$goal_date) {
        user_id
        target
        meet
        goal_date
        created_at
      }
      work_tag
      region_id
      branch
      status
      activityStatus
      notification_via
      remainder_before
      remainder_period_times
      is_admin
      last_login
      last_login_ip
      token_last_created
      
      loadInfoAssignment{
        data{
          username
          id
        
        }
      }
    
      my_profile{
        id
        username
        name
        email
        photo_link
        hris_link
        smscast_link
        mobile
        designation
        branch
        department
        gender
        designation
        worksplace_link
        gender
        sub_department
        full_address
      }
      summary{
        pending
        successful
        fail
      }
      }
      configurations {
        followup_status
        load_type
        network_type
        work_tag
        olt_type
      }
      
        followUpPrelistHierarchicalRemarks{
          id
          req_path
        }
      
      followPreLists{
        id
        text
      }
     
        allPlayPlan{
        pay_plan
        description
      }
      allRegion{
        id
        name
      }
}
"""
        variables = {
        "goal_date": "2024-05-29"
      }
        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='GoalDate')
        GraphQLUser.getTimeStamp("Response of GoalDate", response.status_code)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")
    @task
    def reassignedList(self):#9
        query = """ query($goal_date:Date!){
  me {
      id
      username
      branches{
        branch_id,
        userid
      }
      goal(goal_date:$goal_date) {
        user_id
        target
        meet
        goal_date
        created_at
      }
      work_tag
      region_id
      branch
      status
      activityStatus
      notification_via
      remainder_before
      remainder_period_times
      is_admin
      last_login
      last_login_ip
      token_last_created
      
      loadInfoAssignment{
        data{
          username
          id
        
        }
      }
    
      my_profile{
        id
        username
        name
        email
        photo_link
        hris_link
        smscast_link
        mobile
        designation
        branch
        department
        gender
        designation
        worksplace_link
        gender
        sub_department
        full_address
      }
      summary{
        pending
        successful
        fail
      }
      }
      configurations {
        followup_status
        load_type
        network_type
        work_tag
        olt_type
      }
      
        followUpPrelistHierarchicalRemarks{
          id
          req_path
        }
      
      followPreLists{
        id
        text
      }
     
        allPlayPlan{
        pay_plan
        description
      }
      allRegion{
        id
        name
      } 
}
"""
        variables = {
        "id": 1,
        "username": "",
        "branch": [],
        "load_id": 1
      }
        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='ReassignedList')
        GraphQLUser.getTimeStamp("Response of ReassignedList", response.status_code)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")
    def BalanceQuery(self):#10
        query = """query ($username: String!) {
  CustomerBalanceQuery(username: $username) {
    balance
    __typename
  }
}
"""
        variables = {
        "username": "yunish1"
      }
        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='BalanceQuery')
        GraphQLUser.getTimeStamp("Response of BalanceQuery", response.status_code)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")
    @task()
    def activityStatus(self):#11
        query ="""{
  me {
    id
    work_tag
    activityStatus
    unReadNotification {
      notification_id
      notification_at
      message
      type
      username
      main_id
      notification_id
      user_profile {
        photo_link
        gender
        id
        __typename
      }
      __typename
    }
    __typename
  }
}
"""
        variables ={
        }
        headers = {"Authorization": f"Bearer {self.get_next_token()}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='ActivityStatus')
        GraphQLUser.getTimeStamp("Response of ActivityStatus", response.status_code)
        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")
