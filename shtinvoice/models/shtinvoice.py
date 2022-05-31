from odoo import models,fields, api



class SHT_delivery(models.Model):
    _name= "sht.delivery"
    
    # name=fields.Char(string="Customer Name:")
    name=fields.Many2one("res.partner",string="Customer Name")
    add=fields.Char(related='name.city',string="Address")
    date =fields.Date(string="Date")
    vessel=fields.Char("Vessel :")
    co= fields.Char("C/O") 
    po_no= fields.Integer("PO No.")
    order_no= fields.Integer("Delivery Order No")
    pic= fields.Integer("PIC")
    tel= fields.Char(related='name.phone',string="Tel")


    product_ids=fields.One2many(comodel_name="sht.product", string="Item Name",inverse_name="sr_id")

    
class SHT_product(models.Model):
    _name="sht.product"
    name=fields.Integer("Sr.No.")
    product_id=fields.Many2one("product.product",string="Product Name")

    pro_desc= fields.Text(string="Product Description")
    qut=fields.Integer("Quantity")
    list_price= fields.Float(related='product_id.list_price',string="Price")

    sr_id= fields.Many2one("sht.delivery",string="Sr.No.")

    @api.depends('list_price','qut')
    @api.onchange('list_price' or 'qut')
    def cal_total(self):
        for rec in self:
            print(len(self))
            rec.total_price= rec.list_price * rec.qut

    total_price=fields.Float("Total", compute=cal_total,store=True)

class SHT_order(models.Model):
    _name="sht.order"

    name=fields.Char("Customer Name")
    
    # date= fields.Date("Date")
    product_ids=fields.One2many(comodel_name="sht.product", string="Item Name",inverse_name="product_id")
    # product_id=fields.Char(related='product_ids.product_id',string="Product")
    desc=fields.Text(string="Item Desc.") # related="product_ids.pro_desc", 
    price=fields.Float(related='product_ids.list_price')


class SHT_invoice(models.Model):
    _name='sht.invoice'

    name=fields.Many2one("res.partner",string="Customer Name") # To
    date =fields.Date(string="Date") # date
    invoice_no=fields.Integer("Invoice No") # Invoice No
    order_no=fields.Integer("Order No") # YOUR ORDER NO:
    ref=fields.Char("REF ") #  OUR REF:
    terms= fields.Char("Terms") # Terms
    vender_code= fields.Char("Vendor Code") # vendor code
    job_id= fields.Char("Job ID") # job id
    attn=fields.Char("ATTN") # ATTN

    item_ids=fields.One2many(comodel_name="sht.co_invoice", string="Item Name",inverse_name="item_id")


    # Under Development to calculate Subtotal

    # @api.depends('item_ids')
    # @api.onchange('item_ids')
    # def cal_subtotal(self):
    #     for rec in self:
    #         for item in self.item_ids:
    #             rec.sub_total+=rec.item_ids.amount
    #     self.sub_total=rec.sub_total

    # sub_total=fields.Float("Sub Total",compute=cal_subtotal,store=True)



class SHT_co_invoice(models.Model):
    _name='sht.co_invoice'

    name= fields.Text("Description") # DESCRIPTION	
    # name=fields.Integer("Sr.No.")
    # item= fields.Many2one("product.product",string="Product Name")
    
    qut= fields.Float("QTY/HOUR") # QTY/HOUR
    unit_price= fields.Float("Unit Price") #UNIT PRICE
    	

    @api.depends('qut','unit_price')
    def cal_amount(self):
        for rec in self:
            rec.amount= rec.unit_price * rec.qut

    amount=fields.Float(string='Amount',compute=cal_amount,store=True) #AMOUNT

    item_id= fields.Many2one("sht.invoice",string="Items")