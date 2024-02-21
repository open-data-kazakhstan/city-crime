from datapackage import Package

package = Package()
package.infer(r"C:\Users\USER\Desktop\practice\city-crime\data\comb.csv")
package.commit()
package.save(r"C:\Users\USER\Desktop\practice\city-crime\datapackage.json")