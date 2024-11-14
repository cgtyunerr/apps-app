import { defineStore } from 'pinia'
import axios from 'axios'

const BASE_URL = 'http://localhost:8000/'

export const useCampaignStore = defineStore('campaignStore', {
  state: () => ({
    campaigns: [],
  }),
  actions: {
    async getCampaigns() {
      try {
        const response = await axios.get(`${BASE_URL}campaign/all`, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        this.campaigns = response.data
        console.log(response.data)
      } catch (error) {
        console.error('Failed to fetch assets:', error)
      }
    },

    async updateCampaign(campaign_id, active) {
      try {
        await axios.put(`${BASE_URL}asset/${campaign_id}`, {
          campaign_id: campaign_id,
          active: active,
        })

        this.campaigns.forEach((campaign) => {
          if (campaign.id === campaign_id) {
            campaign.active = false
          }
        })
      } catch (error) {
        console.error('Failed to update campaign:', error)
      }
    },
  },
})
