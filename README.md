# 📌 Patrones de Diseño

## 📖 Descripción
Este repositorio contiene implementaciones y explicaciones detalladas sobre patrones de diseño fundamentales en la programación orientada a objetos. Cada patrón incluye una descripción clara de su propósito y cuándo debe utilizarse para facilitar su comprensión.

---

## 🔹 Factory Method
### 📌 Propósito
El patrón Factory Method define una interfaz para la creación de objetos, pero permite que las subclases alteren el tipo de objetos que se crean. Facilita la encapsulación de la lógica de instanciación y promueve la reutilización del código.

### 📌 Cuándo Usarlo
- Cuando una clase no puede anticipar el tipo exacto de objetos que debe crear.
- Cuando se desea delegar la creación de objetos a subclases para lograr un diseño más flexible.
- Para simplificar la creación de objetos y evitar la dependencia directa de clases concretas.

---

## 🔹 Strategy
### 📌 Propósito
El patrón Strategy permite definir una familia de algoritmos, encapsular cada uno de ellos y hacerlos intercambiables sin alterar el código cliente. Ayuda a separar la lógica de selección de algoritmos del código principal.

### 📌 Cuándo Usarlo
- Cuando se tienen múltiples maneras de realizar una operación y se quiere cambiar la implementación en tiempo de ejecución.
- Para evitar múltiples condicionales dentro de una misma clase.
- Cuando se desea encapsular la lógica de diferentes estrategias de manera independiente.

---

## 🔹 Decorator
### 📌 Propósito
El patrón Decorator permite agregar funcionalidades adicionales a objetos de manera dinámica sin modificar su estructura original. Es una alternativa flexible a la herencia para extender el comportamiento de los objetos.

### 📌 Cuándo Usarlo
- Cuando se necesita extender funcionalidad sin modificar la clase original.
- Para evitar una jerarquía de herencia demasiado compleja.
- Cuando se desea añadir comportamientos en tiempo de ejecución de manera flexible.

---

## 🔹 Composite
### 📌 Propósito
El patrón Composite permite tratar objetos individuales y estructuras de objetos de manera uniforme dentro de una jerarquía en forma de árbol. Facilita la gestión de objetos complejos con estructuras recursivas.

### 📌 Cuándo Usarlo
- Cuando se necesita representar una jerarquía de objetos de forma uniforme.
- Cuando se quiere tratar objetos individuales y compuestos de la misma manera.
- Para estructurar elementos en árboles de composición sin afectar su manipulación.

---

## 🚀 Instalación y Uso
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/design-patterns.git
   ```
2. Explora los ejemplos dentro de cada patrón.
3. Ejecuta los ejemplos en tu entorno preferido.

---

## 📌 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas agregar mejoras o ejemplos en otros lenguajes, abre un issue o un pull request.

---

## 📝 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

