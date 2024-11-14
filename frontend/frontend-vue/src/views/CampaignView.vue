<template>
  <b-container class="bv-example-row">
    <b-row class="py-3 align-items-center">
      <b-col sm="7">
        <h3 class="p-0 m-0">Campaigns</h3>
      </b-col>
    </b-row>
    <b-row class="pt-5">
      <b-col sm="12">
        <b-table bordered striped hover :items="campaignStore.campaigns" :fields="fields">
          <template #cell(actions)="row">
            <button type="button" class="btn btn-primary" @click="showModal(row)">Open</button>
            <b-modal v-model="modalOpen" hide-footer centered hide-header>
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="m-0">Campaign {{ selectedRow }}</h5>
                <button
                  type="button"
                  class="close rounded-circle"
                  aria-label="Close"
                  @click="modalOpen = false"
                >
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="d-block text-center">
                <b-row>
                  <div class="assign-asset-container">
                    <div class="assign-asset-container">
                      <h3>Assign Asset</h3>
                      <b-form-group label="">
                        <div class="d-flex align-items-center">
                          <b-dropdown
                            id="dropdown-1"
                            text="Select Assets"
                            class="m-md-2"
                            variant="outline-primary"
                            multiple
                          >
                            <b-dropdown-item
                              v-for="asset in campaignCreativeStore.assets"
                              :key="asset.id"
                            >
                              <b-form-checkbox v-model="selectedAssets" :value="asset.id">
                                {{ asset.id }} - {{ asset.title }} - {{ asset.status }}
                              </b-form-checkbox>
                            </b-dropdown-item>
                            <b-dropdown-divider></b-dropdown-divider>
                          </b-dropdown>
                          <b-button variant="primary" @click="assignAsset"
                            >Assign Selected Asset</b-button
                          >
                        </div>
                      </b-form-group>
                    </div>
                  </div>
                  <h3 class="p-0 m-0 small text">Campaign Creatives</h3>
                  <div>
                    <b-table
                      bordered
                      striped
                      hover
                      :items="campaignCreativeStore.campaignCreatives"
                      :fields="modal_fields"
                    >
                      <template #cell(actions)="row">
                        <input type="checkbox" v-model="row.item.check" />
                      </template>
                    </b-table>
                    <div class="mt-3 text-center">
                      <b-button variant="primary" @click="UnassignSelectedCreatives">
                        Unssign Selected Creatives
                      </b-button>
                    </div>
                  </div>
                </b-row>
              </div>
              <b-button class="mt-3" block @click="modalOpen = false">Close</b-button>
            </b-modal>
          </template>
        </b-table>
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCampaignStore } from '@/stores/campaignStore'
import { useCampaignCreativeStore } from '@/stores/campaignCreativeStore'

const campaignStore = useCampaignStore()
const campaignCreativeStore = useCampaignCreativeStore()

const fields = [
  { key: 'service_campaign_id', label: 'ID' },
  { key: 'title', label: 'Title' },
  { key: 'active', label: 'Active' },
  { key: 'created_at', label: 'Created_at' },
  { key: 'actions', label: 'Actions' },
]

const modal_fields = [
  { key: 'id', label: 'ID' },
  { key: 'asset_id', label: 'Asset ID' },
  { key: 'status', label: 'Status' },
  { key: 'actions', label: '' },
]

const selectedAssets = ref([])
const selectedRow = ref(0)
const selectedCreatives = ref([])

onMounted(() => {
  campaignStore.getCampaigns()
})

function assignAsset() {
  campaignCreativeStore.assignCampaignCreatives(selectedRow.value, selectedAssets.value)
  this.selectedAssets.length = 0
}

function UnassignSelectedCreatives() {
  campaignCreativeStore.unassignCampaignCreatives(
    selectedRow.value,
    campaignCreativeStore.campaignCreatives.filter((a) => a.check === true).map((a) => a.id),
  )
}

const modalOpen = ref(false)

function showModal(row) {
  selectedAssets.value.length = 0
  selectedCreatives.value.length = 0
  campaignCreativeStore.campaignCreatives.length = 0
  modalOpen.value = true
  selectedRow.value = row.item.service_campaign_id
  campaignCreativeStore.getCampaignCreatives(row.item.service_campaign_id)
  campaignCreativeStore.getAssets()
}
</script>

<style scoped></style>
