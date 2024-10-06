import shapefile
import pyproj
import openpyxl

cc = [18.664, 19.417, -95.612, -96.897]  # ymin, ymax, xmin, xmax

file_1 = "hidro4mcw.shp"
sf = shapefile.Reader(file_1)

shapes = sf.shapes()
records = sf.records()
fields = sf.fields[1:]

filtered_shapes = []
filtered_records = []


def read_prj_file(prj_filepath):
    with open(prj_filepath, 'r') as prjfile:
        return prjfile.read()


prj_file = "hidro4mcw.prj"
wkt = read_prj_file(prj_file)
proj = pyproj.CRS.from_wkt(wkt)
transformer = pyproj.Transformer.from_crs(proj, "EPSG:4326", always_xy=True)


def write_bounding_boxes_to_excel(shapes, transformer, excel_filename):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Bounding Boxes"
    headers = ['Shape Index', 'Min Lon', 'Min Lat', 'Max Lon', 'Max Lat']
    sheet.append(headers)
    for index, f_shape in enumerate(shapes):
        shape_bbox = f_shape.bbox
        shape_min_x, shape_min_y, shape_max_x, shape_max_y = shape_bbox
        shape_min_lon, shape_min_lat = transformer.transform(shape_min_x, shape_min_y)
        shape_max_lon, shape_max_lat = transformer.transform(shape_max_x, shape_max_y)
        row_data = [index, shape_min_lon, shape_min_lat, shape_max_lon, shape_max_lat]
        sheet.append(row_data)
    workbook.save(excel_filename)
    print(f"Bounding boxes successfully written to {excel_filename}")


excel_filename = "excelnuevo.xlsx"
write_bounding_boxes_to_excel(shapes, transformer, excel_filename)