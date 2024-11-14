import { defineStore } from 'pinia'
import axios from 'axios'

const BASE_URL = 'http://localhost:8000/'

export const useCampaignCreativeStore = defineStore('campaignCreativeStore', {
  state: () => ({
    campaignCreatives: [],
    assets: [],
  }),
  actions: {
    async getCampaignCreatives(campaign_id) {
      try {
        const response = await axios.get(`${BASE_URL}campaign-creative/all`, {
          params: {
            campaign_id: campaign_id,
          },
        })
        this.campaignCreatives = response.data
        this.campaignCreatives.forEach((element) => {
          element.check = false
        })
      } catch (error) {
        console.error('Failed to fetch assets:', error)
      }
    },

    async assignCampaignCreatives(campaign_id, asset_ids) {
      try {
        const response = await axios.post(`${BASE_URL}campaign-creative/assign`, {
          campaign_id: campaign_id,
          asset_ids: asset_ids,
        })

        this.campaignCreatives.push(...response.data)
      } catch (error) {
        console.error('Failed to update campaign:', error)
      }
    },

    async unassignCampaignCreatives(campaign_id, creative_ids) {
      try {
        await axios.post(`${BASE_URL}campaign-creative/unassign`, {
          campaign_id: campaign_id,
          creative_ids: creative_ids,
        })

        this.campaignCreatives = this.campaignCreatives.filter((a) => !creative_ids.includes(a.id))
      } catch (error) {
        console.error('Failed to update campaign:', error)
      }
    },
    async getAssets() {
      try {
        const response = await axios.get(`${BASE_URL}asset/all/`, {
          headers: {
            'Content-Type': 'application/json',
          },
        })
        this.assets = response.data
      } catch (error) {
        console.error('Failed to fetch assets:', error)
      }
    },
  },
})
