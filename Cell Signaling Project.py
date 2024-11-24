print(f'Choose a signaling molecule:')
print(f'1. Steroid Hormone')
print(f'2. Peptide Hormone')
choice = input(f'Enter 1 for Steriod Hormone or 2 for Peptide Hormone: ')
if choice == 1: 
    signalingMolecule = ['small', 'nonpolar', 'hydrophobic']
elif choice == 2:
    signalingMolecule = ['large', 'polar', 'hydrophilic']
    print(f'Choose a receptor type:')
    print(f'1. GProtein')
    print(f'2. Ligand')
    receptor_choice = input(f'Enter 1 for GProtein or 2 for Ligand: ')
    if receptor_choice == 1:
        receptorType = 'GProtein'
    elif receptor_choice == 2:
        receptorType = 'Ligand'
    else:
        print(f'Invalid recepetor choice! Please restart the program and enter 1 or 2.')
        exit()
else: 
    print(f'Invalid choice! Please restart the program and enter 1 or 2.')
    exit()


def cellSignaling(signalingMolecule, receptorType=None):
    steroidHormone = ["small", "nonpolar", "hydrophobic"] 
    peptideHormone = ["large", "polar", "hydrophilic"] #lists are characteristics from notes
#Reception
    if signalingMolecule == steroidHormone:
        def intracellularReceptor():
            print("Crossing membrane and moving to Transduction phase.")
            return
        intracellularReceptor()
    elif signalingMolecule == peptideHormone: 
        def membraneReceptor(receptorType):        
            if receptorType == 'GProtein':
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
                        return
                    
            LigandReceptor = (receptorType == 'Ligand')
            if LigandReceptor:
                def Ligand(): 
                    print('Binding to ligand-gated ion channel receptor.')
                    gateOpens = True
                if gateOpens == True:  
                    print('Na+ and Ca2+ go through ion channel and go to transduction.')
                    ligandUnbinds = True
                if ligandUnbinds: 
                    gateOpens = False
                    return
    elif signalingMolecule not in [steroidHormone, peptideHormone]: 
        print('Invalid signaling molecule.')
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
            return
        
    def secondMessengers(): 
        secondMessenger = True
        if secondMessenger == True:
            proteinActive = True
            phosphorylationCascade()
            return
            
#Response
    transcriptionFactor = False
    def createProtein():
        transcriptionFactor = True
        print('Begins transcription and translation, then goes to the ribosome.')
    createProtein()
    return

    def inactivateProtein():
        transcriptionFactor = False
        print('Inhibits protein by competitive or noncompetitive inhibition.')
        return
    inactivateProtein()
    
cellSignaling("peptideHormone")