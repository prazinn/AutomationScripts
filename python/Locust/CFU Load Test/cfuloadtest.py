from locust import HttpUser, task, between
import json
from datetime import datetime

class GraphQLUser(HttpUser):
    host = "https://cfu-gateway.wlink.com.np"
    wait_time = between(1, 5)

    def getTimeStamp(message, statuscode):
        print(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"), message, statuscode)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsb2dpbi53bGluay5jb20ubnAiLCJpYXQiOjE3MTYxOTI4MTcsImV4cCI6MTcxNjMwODAyNSwibmJmIjoxNzE2MjcyMDI1LCJqdGkiOiJMenZtbGdCZGI3RXBJUzM3Iiwic3ViIjoicHJhamluLnNocmVzdGhhIiwiYXVkIjoiZmEtdHJhY2tpbmcud2xpbmsuY29tLm5wIn0.5IPqZ9KCYd_z8XOiM1LU08AVWzzXQxR7c30Ia_soKcI"

    @task
    def user(self):
        query = """
        {
          me {
            username
          }
        }
        """
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query}, headers=headers, name="UserAPI")
        GraphQLUser.getTimeStamp("Response of user", response.status_code)
        print(response.text)

        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def load_disable(self):
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

        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='LoadDisable API')
        GraphQLUser.getTimeStamp("Response of Load Disable", response.status_code)
        print(response.text)

        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def load_proactive(self):
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

        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='LoadProactive API')
        GraphQLUser.getTimeStamp("Response of ProActive", response.status_code)
        print(response.text)

        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def courtesy_follow_up(self):
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

        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='CourtesyFollowUp API')
        GraphQLUser.getTimeStamp("Response of CourtesyFollowUp", response.status_code)
        print(response.text)

        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")

    @task
    def beacon_trial(self):
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

        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='BeaconTrial API')
        GraphQLUser.getTimeStamp("Response of BeaconTrial", response.status_code)
        print(response.text)

        if response.status_code != 200:
            response.failure(f"Failed to query GraphQL API: {response.text}")
    @task()
    def dashboardapi1(self):
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
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='ActiveCustomerCounts')
        GraphQLUser.getTimeStamp("Response of DashboardAPI1", response.status_code)
        print(response.text)
    @task
    def clientlist(self):
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
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='ClientList')
        GraphQLUser.getTimeStamp("Response of ClientList", response.status_code)
    @task
    def loadinfos(self):
        query = """
        query ($first: Int, $page: Int, $filter: LoadInfoAssignMentFilter, $followUp: QueryLoadinfosFollowUpWhereHasConditions, $where: QueryLoadinfosWhereWhereConditions) {
          myuser: me {
            id
            __typename
          }
          statusList: configurations {
            followup_status
            __typename
          }
          loadinfos(first: $first, page: $page, filter: $filter, where: $where, followUp: $followUp) {
            paginatorInfo {
              count
              currentPage
              hasMorePages
              firstItem
              lastItem
              lastPage
              perPage
              total
              __typename
            }
            data {
              id
              entry_source
              current_assignment
              transfer_from_proactive
              username
              client_name
              olt_name
              client_number
              grace_status
              courtesy_followup_range
              nettv
              support_zone
              assignment_branch
              max_days
              days_remaining
              address
              load_type
              updated_at
              created_at
              total_comments
              unique_identifier
              disabledate: disabled_days
              status: current_status
              acceptStatus: current_status
              churn_probable_flag
              latestComment {
                remarks
                preList {
                  id
                  text
                  __typename
                }
                __typename
              }
              currentAssignment {
                username
                __typename
              }
              plan_name
              __typename
            }
            __typename
          }
        }
        """
        
        variables = {
            "first": 50,
            "page": 1,
            "filter": {
                "currentAssignmentBranchId": 26,
                "currentAssignmentUserId": 20832,
                "includeCurrentStatus": [
                    "assigned",
                    "reassigned",
                    "accepted"
                ],
                "createdDuration": {
                    "from": "2024-05-21",
                    "to": "2024-05-28"
                },
                "isFirstPaymentLoad": "n"
            },
            "branch": 26
        }
        
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='LoadInfos')
        GraphQLUser.getTimeStamp("Response of LoadInfos", response.status_code)
        print(response.text)
    @task
    def loadinfos(self):
        query = """
        query ($branch: [Int]) {
          reassignedList: userByBranch(filter: {branch: $branch, status: y, workTag: [customer_account_followUp_team, customer_account_disable_followup_team, customer_account_proactive_followup_team, courtesy_followup_team, beacon_trial_followup_team]}) {
            username
            id
            work_tag
            activityStatus
            name
            photo_link
            gender
            __typename
          }
        }

        """
        
        variables = {
          "first": 50,
          "page": 1,
          "filter": {
            "currentAssignmentBranchId": 26,
            "currentAssignmentUserId": 20832,
            "includeCurrentStatus": [
              "assigned",
              "reassigned",
              "accepted"
            ],
            "createdDuration": {
              "from": "2024-05-21",
              "to": "2024-05-28"
            },
            "isFirstPaymentLoad": "n"
          },
          "branch": 26
        }
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.client.post("/graphql", json={'query': query, 'variables': variables}, headers=headers, name='LoadInfos')
        GraphQLUser.getTimeStamp("Response of LoadInfos", response.status_code)
        print(response.text)

