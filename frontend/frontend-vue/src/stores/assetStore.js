import { defineStore } from 'pinia'
import axios from 'axios'

const BASE_URL = 'http://localhost:8000/'

export const useAssetStore = defineStore('assetStore', {
  state: () => ({
    assets: [],
  }),
  actions: {
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
    async addAsset(files) {
      try {
        const formData = new FormData()
        for (let i = 0; i < files.length; i++) {
          formData.append('files', files[i])
        }
        const response = await axios.post(`${BASE_URL}asset/create/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })

        this.assets.push(...response.data)
      } catch (error) {
        console.error('Failed to upload assets:', error)
      }
    },

    async removeAsset(asset) {
      try {
        await axios.delete(`${BASE_URL}asset/${asset.id}`)

        this.assets = this.assets.filter((a) => a.id !== asset.id)
      } catch (error) {
        console.error('Failed to remove asset:', error)
      }
    },
  },
})
