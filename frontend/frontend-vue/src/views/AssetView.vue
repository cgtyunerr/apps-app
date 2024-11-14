<template>
  <b-container class="bv-example-row">
    <b-row class="py-3 aling-items-center">
      <b-col sm="7">
        <h3 class="p-0 m-0">Assets</h3>
      </b-col>
      <b-col sm="5" class="d-flex align-items-center">
        <input type="file" @change="onFileChange" multiple />

        <b-button @click="uploadImage" variant="outline-primary">Upload</b-button>
      </b-col>
    </b-row>
    <b-row class="pt-5">
      <b-col sm="12">
        <b-table bordered striped hover :items="assetStore.assets" :fields="fields">
          <template #cell(actions)="data">
            <b-button size="sm" variant="danger" @click="deleteAsset(data.item)"> Delete </b-button>
          </template>
        </b-table>
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAssetStore } from '@/stores/assetStore'

const assetStore = useAssetStore()
const selectedFile = ref(null)

const fields = [
  { key: 'id', label: 'ID' },
  { key: 'title', label: 'Title' },
  { key: 'status', label: 'Status' },
  { key: 'created_at', label: 'Created_at' },
  { key: 'actions', label: 'Actions' },
]

onMounted(() => {
  assetStore.getAssets()
})

const onFileChange = (event) => {
  selectedFile.value = event.target.files
}

const uploadImage = () => {
  if (selectedFile.value) {
    assetStore.addAsset(selectedFile.value)
  } else {
    alert('Please select an image')
  }
}

const deleteAsset = (asset) => {
  try {
    assetStore.removeAsset(asset)
  } catch (e) {
    alert(e)
  }
}
</script>

<style scoped></style>
