steroidHormone = ["small", "nonpolar", "hydrophobic"] 
peptideHormone = ["large", "polar", "hydrophilic"] #lists are characteristics from notes

def cellSignaling():
#Reception
    print(f'Choose a signaling molecule:')
    print(f'1. Steroid Hormone')
    print(f'2. Peptide Hormone')
    choice = int(input(f'Enter 1 for Steriod Hormone or 2 for Peptide Hormone: '))
    
    if choice == 1: 
        signalingMolecule = steroidHormone
        print(f'You have chosen a Steroid Hormone.')
        def intracellularReceptor():
            print("Crossing membrane and moving to Transduction phase.")
        intracellularReceptor()
    elif choice == 2:
        signalingMolecule = peptideHormone
        def membraneReceptor():   
            print(f'Choose a receptor type:')
            print(f'1. GProtein')
            print(f'2. Ligand')
            receptor_choice = int(input(f'Enter 1 for GProtein or 2 for Ligand: '))
            
            if receptor_choice == 1:    
                receptorType = 'GProtein'
                def GProtein():
                    print('Binding to GPCR.')
                    bindToGTP = True
                    if bindToGTP:
                        print('Activating G-Protein.')
                        activateGProtein = True
                        if activateGProtein:
                            print('Activating enzyme.')
                            activatedEnzyme = True
                    if activatedEnzyme == True: 
                        print("Moving to transduction phase.")
                GProtein()
            elif receptor_choice == 2:
                receptorType = 'Ligand'
                def Ligand(): 
                    print('Binding to ligand-gated ion channel receptor.')
                    gateOpens = True
                    if gateOpens == True:  
                        print('Na+ and Ca2+ go through ion channel and go to transduction.')
                        ligandUnbinds = True
                    if ligandUnbinds: 
                        gateOpens = False
                Ligand()
            else: 
                print(f'Invalid recepetor choice! Please restart and enter 1 or 2.')
        membraneReceptor()
            
    else: 
        print(f'Invalid choice! Please restart the program.')
        return
    
#Transduction
    def phosphorylationCascade(): 
        proteinActive = False
        if proteinActive == False: 
            def activateProtein(): #phosphorylation
                nonlocal proteinActive
                proteinActive = True
                print('Protein kinase transfers phosphate to ATP.')  
                proteinActive == True
            activateProtein()            
        elif proteinActive == True: 
            def deactivateProtein(): 
                nonlocal proteinActive
                proteinActive = False
                print('Protein phosphatases remove a phosphate from protein, turn off the transduction pathway, and enable protein kinase for reuse.')
            deactivateProtein()
    phosphorylationCascade()
    
    def secondMessengers(): 
        secondMessenger = True
        if secondMessenger == True:
            proteinActive = True
            phosphorylationCascade()
    secondMessengers()
    
#Response
    transcriptionFactor = False
    def createProtein():
        transcriptionFactor = True
        print('Begins transcription and translation, then goes to the ribosome.')
    createProtein()
    
    def inactivateProtein():
        transcriptionFactor = False
        print('Inhibits protein by competitive or noncompetitive inhibition.')
        return
    inactivateProtein()
    
cellSignaling()