from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

from assetsapp.models import Asset


class AssetViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Asset.objects.create(
            name = 'PC',
            serial = '123a',
            purchase_price = 1000000,
            purchase_date = timezone.now(),
            current_status = 'AV'
        )
    
    def setUp(self):
        self.asset = Asset.objects.get(pk=1)
        self.assets_url = reverse('assetsapp:assets')
        self.detail_url = reverse('assetsapp:asset_detail', args=(self.asset.id,))
        self.create_url = reverse('assetsapp:asset_create')

    # AssetView()
    def test_asset_view_is_working_with_correct_template(self):
        response = self.client.get(self.assets_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'assetsapp/asset.html')

    def test_asset_view_list_all_assets(self):
        response = self.client.get(self.assets_url)
        self.assertTrue(len(response.context['filter'].qs) == 1)
    
    # AssetDetail()
    def test_detail_view_is_working_with_correct_template(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'assetsapp/asset_detail.html')

    def test_detail_view_displays_an_specific_asset(self):
        response = self.client.get(self.detail_url)
        self.assertContains(response, self.asset.name)

    #AssetCreate()
    def test_create_view_adds_a_new_asset(self):
        response = self.client.post(
            path = self.create_url,
            data = {
                'name': 'Tablet',
                'serial': '123b',
                'purchase_price': 2249900,
                'purchase_date': timezone.now(),
                'current_status': 'AV',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'assetsapp/asset_form.html')
