from AddProduct.AddProductDAO import AddProductDAO
from AddProduct.AddProductPresenter import AddProductPresenter
from AddProduct.AddProductUseCase import AddProductUseCase
from AddProduct.AddProductView import AddProductView
from FindProduct.FindProductDAO import FindProductDAO
from FindProduct.FindProductPresenter import FindProductPresenter
from FindProduct.FindProductUseCase import FindProductUseCase
from FindProduct.FindProductView import FindProductView
from FindProduct.viewModel.FindProductHangHoaViewModel import FindProductHangHoaViewModel
from GetProductList.GetProductListPresenter import GetProductListPresenter
from GetProductList.GetProductListDAO import GetProductListDAO
from GetProductList.GetProductListUseCase import GetProductListUseCase
from GetTypeList.GetTypeListDAO import GetTypeListDAO
from GetTypeList.GetTypeListPresenter import GetTypeListPresenter
from GetTypeList.GetTypeListUseCase import GetTypeListUseCase
from MainController import MainController
from ModifyProduct.ModifyProductDAO import ModifyProductDAO
from ModifyProduct.ModifyProductUseCase import ModifyProductUseCase
from ModifyProduct.ModifyProductView import ModifyProductView
from RemoveProduct.RemoveProductDAO import RemoveProductDAO
from RemoveProduct.RemoveProductPresenter import RemoveProductPresenter
from RemoveProduct.RemoveProductUseCase import RemoveProductUseCase
from RemoveProduct.RemoveProductView import RemoveProductView
from View import View

if __name__ == "__main__":
    # Khởi tạo các thành phần
    getProductListViewModel = []
    getProductListPresenter = GetProductListPresenter(getProductListViewModel)
    getProductListDAO = GetProductListDAO()
    getProductListUseCase = GetProductListUseCase(getProductListDAO, getProductListPresenter)

    getTypeListViewModel = []
    getTypeListPresenter = GetTypeListPresenter(getTypeListViewModel)
    getTypeListDAO = GetTypeListDAO()
    getTypeListUseCase = GetTypeListUseCase(getTypeListDAO, getTypeListPresenter)

    findProductHangHoaViewModel: FindProductHangHoaViewModel = None
    findProductPresenter = FindProductPresenter(findProductHangHoaViewModel)
    findProductDAO = FindProductDAO()
    findProductUseCase = FindProductUseCase(findProductDAO, findProductPresenter)
    findProductView = FindProductView()

    removeProductDAO = RemoveProductDAO()
    removeProductPresenter = RemoveProductPresenter()
    removeProductUseCase = RemoveProductUseCase(removeProductDAO, removeProductPresenter)

    addProductPresenter = AddProductPresenter()
    addProductDAO = AddProductDAO()
    addProductUseCase = AddProductUseCase(addProductDAO, addProductPresenter)

    modifyProductPresenter = AddProductPresenter()
    modifyProductDAO = ModifyProductDAO()
    modifyProductUseCase = ModifyProductUseCase(modifyProductPresenter,modifyProductDAO)

    controller = MainController(getProductListUseCase, getTypeListUseCase, findProductUseCase, removeProductUseCase,
                                addProductUseCase, modifyProductUseCase)
    addProductView = AddProductView(controller)

    removeProductView = RemoveProductView(controller)

    modifyProductView = ModifyProductView(controller)
    view = View(addProductView, findProductView, removeProductView, modifyProductView, controller)

    getProductListPresenter.attach(view)
    getTypeListPresenter.attach(view)
    getTypeListPresenter.attach(addProductView)
    findProductPresenter.attach(findProductView)
    findProductPresenter.attach(removeProductView)
    removeProductPresenter.attach(removeProductView)
    addProductPresenter.attach(addProductView)
    findProductPresenter.attach(modifyProductView)

    controller.executeGetProductListUseCase()
    controller.executeGetTypeListUseCase()

    view.frame.mainloop()
